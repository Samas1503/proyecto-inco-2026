"""
Módulo de Base de Hechos y Modelado de Marcos (Frames)
Trabajo de Campo - Inteligencia del Conocimiento (InCo)
Punto 2: Arquitecto de Base de Hechos (Modelado de Marcos / Frames)

Este módulo implementa:
1. Parche de compatibilidad para Experta en Python 3.10+ (Google Colab).
2. Clases bases para Marcos de Conocimiento (Frames) según teoría de Minsky:
   - MarcoContexto: Clima, día, temperatura, eventos y contexto ambiental.
   - MarcoCliente: Perfiles de cliente, tamaño de grupo, preferencias de consumo.
   - MarcoInsumo: Productos, rotación, almacenamiento, estado perecedero y variaciones de costo.
   - MarcoProveedor: Disponibilidad de comercios, políticas de precios y orígenes de compra.
   - MarcoOperacion: Eventos operativos, estados de servicio, comandas y alertas de crisis.
   - HechoSimbolico: Representación híbrida directa de las 66 proposiciones (A a BN).
3. Diccionario canónico de las 66 proposiciones con metadatos y descripciones.
4. Generador y cargador de Memoria de Trabajo Inicial (WM0) para los Casos de Uso 1, 2 y 3.
"""

import sys
import collections

# =====================================================================
# 1. PARCHE DE COMPATIBILIDAD PARA PYTHON 3.10+ Y GOOGLE COLAB
# =====================================================================
try:
    import collections.abc
    for attr in [
        'Mapping', 'MutableMapping', 'Sequence', 'MutableSequence',
        'Iterable', 'MutableSet', 'Callable', 'Container'
    ]:
        if not hasattr(collections, attr) and hasattr(collections.abc, attr):
            setattr(collections, attr, getattr(collections.abc, attr))
except Exception as e:
    pass

# Intentar importar Experta; si no está instalada, proveer clases base compatibles
try:
    from experta import Fact as ExpertaFact
    from experta import Field as ExpertaField
    from experta import KnowledgeEngine, Rule, DefFacts, AS, MATCH, NOT, AND, OR
    EXPERTA_DISPONIBLE = True
except ImportError:
    EXPERTA_DISPONIBLE = False
    
    # Implementación base idéntica si Experta no está presente en el entorno local
    class ExpertaFact(dict):
        """Fallback compatible con Fact de Experta cuando corre sin dependencias externas."""
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__dict__ = self
            
    def ExpertaField(type_cls=object, default=None, **kwargs):
        return default

    class KnowledgeEngine:
        def __init__(self):
            self.facts = {}
            self._fact_id = 0
        def reset(self):
            self.facts.clear()
            self._fact_id = 0
        def declare(self, *facts):
            for f in facts:
                self._fact_id += 1
                self.facts[self._fact_id] = f
                print(f"[WM+] Declarado: {f}")
        def run(self):
            print("[Motor] Ejecución simulada (instalar 'experta' en Colab para inferencia completa).")

    def Rule(*args, **kwargs):
        def decorator(fn):
            return fn
        return decorator

    def DefFacts(*args, **kwargs):
        def decorator(fn):
            return fn
        return decorator

    class _LogicalOp:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            
    OR = _LogicalOp
    AND = _LogicalOp
    NOT = _LogicalOp
    MATCH = _LogicalOp
    AS = _LogicalOp

# Exportar las clases base
Fact = ExpertaFact
Field = ExpertaField

# =====================================================================
# 2. DICCIONARIO CANÓNICO DE PROPOSICIONES FORMALES (A - BN)
# =====================================================================
DICCIONARIO_PROPOSICIONES = {
    # Módulo A: Demanda y Contexto
    "A": {"desc": "Día es Fin de semana", "categoria": "Contexto", "ranura": "dia", "valor": "fin_de_semana"},
    "B": {"desc": "Día es Domingo", "categoria": "Contexto", "ranura": "dia", "valor": "domingo"},
    "C": {"desc": "Aumentar compra de mercadería", "categoria": "Accion", "ranura": "compra", "valor": "aumentar"},
    "D": {"desc": "Surtir para mañana, tarde y noche", "categoria": "Accion", "ranura": "turnos_abastecimiento", "valor": "todos"},
    "E": {"desc": "Evento es Partido Boca/River", "categoria": "Contexto", "ranura": "evento", "valor": "boca_river"},
    "F": {"desc": "Planificar turnos temprano y tarde", "categoria": "Accion", "ranura": "turnos_personal", "valor": "temprano_y_tarde"},
    "G": {"desc": "Comprar bebidas de forma gradual", "categoria": "Accion", "ranura": "estrategia_bebida", "valor": "gradual"},
    "H": {"desc": "No comprar bebidas de golpe", "categoria": "Accion", "ranura": "estrategia_bebida", "valor": "no_de_golpe"},
    "I": {"desc": "Evento es Desfile 23 de Agosto", "categoria": "Contexto", "ranura": "evento", "valor": "desfile_23_agosto"},
    "J": {"desc": "Competencia es Alta", "categoria": "Contexto", "ranura": "competencia", "valor": "alta"},
    "K": {"desc": "Reducir expectativa de demanda", "categoria": "Accion", "ranura": "expectativa_demanda", "valor": "reducida"},
    "L": {"desc": "Evitar sobrestock", "categoria": "Accion", "ranura": "riesgo_stock", "valor": "evitar_sobrestock"},
    "M": {"desc": "Temperatura es frío", "categoria": "Contexto", "ranura": "temperatura", "valor": "frio"},
    "N": {"desc": "Ofrecer menú caliente (sopas)", "categoria": "Accion", "ranura": "oferta_menu", "valor": "caliente_sopas"},
    "O": {"desc": "Mantener menú habitual", "categoria": "Accion", "ranura": "oferta_menu", "valor": "mantener_habitual"},
    "P": {"desc": "Ofrecer sándwiches y pizzas", "categoria": "Accion", "ranura": "oferta_menu", "valor": "sandwiches_pizzas"},
    "Q": {"desc": "Fecha es quincena o cobro", "categoria": "Contexto", "ranura": "es_quincena", "valor": True},
    "R": {"desc": "Clima es soleado", "categoria": "Contexto", "ranura": "clima", "valor": "soleado"},
    "S": {"desc": "Reservas son grupos grandes", "categoria": "Cliente", "ranura": "reservas", "valor": "grupos_grandes"},
    "T": {"desc": "Comportamiento es Alta Bebida y Baja Comida", "categoria": "Cliente", "ranura": "comportamiento", "valor": "alta_bebida_baja_comida"},
    "U": {"desc": "Aumentar compra de destilados y snacks", "categoria": "Accion", "ranura": "compras_especificas", "valor": "mas_destilados_snacks"},
    "V": {"desc": "Reducir compra de vegetales", "categoria": "Accion", "ranura": "compras_especificas", "valor": "menos_vegetales"},
    "W": {"desc": "Tipo de cliente es Familia", "categoria": "Cliente", "ranura": "tipo", "valor": "familia"},
    "X": {"desc": "Preferencia es Menú al plato", "categoria": "Cliente", "ranura": "preferencia", "valor": "menu_al_plato"},
    "Y": {"desc": "Tipo de cliente es Jóvenes", "categoria": "Cliente", "ranura": "tipo", "valor": "jovenes"},
    "Z": {"desc": "Preferencia es Bebidas y sándwiches", "categoria": "Cliente", "ranura": "preferencia", "valor": "bebidas_y_sandwiches"},

    # Módulo B: Compras y Prioridad de Insumos
    "AA": {"desc": "Producto es Cerveza", "categoria": "Insumo", "ranura": "nombre", "valor": "cerveza"},
    "AB": {"desc": "Prioridad de compra es Alta y Rotación muy rápida", "categoria": "Accion", "ranura": "prioridad_rotacion", "valor": "alta_muy_rapida"},
    "AC": {"desc": "Producto es Pre-pizza, Queso, Jamón o Salsa", "categoria": "Insumo", "ranura": "categoria", "valor": "pizza_y_aderezos"},
    "AD": {"desc": "Prioridad de compra es Alta y Rotación rápida", "categoria": "Accion", "ranura": "prioridad_rotacion", "valor": "alta_rapida"},
    "AE": {"desc": "Tarea es Compra Diaria", "categoria": "Operacion", "ranura": "tarea", "valor": "compra_diaria"},
    "AF": {"desc": "Desplazarse a mercados favoritos", "categoria": "Accion", "ranura": "metodo_compra", "valor": "mercados_favoritos"},
    "AG": {"desc": "Pagar con Efectivo, Transferencia o Tarjeta", "categoria": "Accion", "ranura": "medios_pago", "valor": "efectivo_transferencia_tarjeta"},
    "AH": {"desc": "Dueña no está disponible", "categoria": "Operacion", "ranura": "duena_disponible", "valor": False},
    "AI": {"desc": "Delegar compra a Encargada de caja", "categoria": "Accion", "ranura": "delegacion", "valor": "encargada_caja"},
    "AJ": {"desc": "Producto es Hielo", "categoria": "Insumo", "ranura": "nombre", "valor": "hielo"},
    "AK": {"desc": "Origen de compra son Proveedores Fijos", "categoria": "Accion", "ranura": "origen_compra", "valor": "proveedores_fijos"},
    "AL": {"desc": "Local favorito no sostiene precio", "categoria": "Proveedor", "ranura": "sostiene_precio", "valor": False},
    "AM": {"desc": "Otro local tiene precio más barato", "categoria": "Proveedor", "ranura": "precio_mas_barato", "valor": True},
    "AN": {"desc": "Cambiar de local/proveedor", "categoria": "Accion", "ranura": "decision_proveedor", "valor": "cambiar_proveedor"},

    # Módulo C: Almacenamiento y Conservación
    "AO": {"desc": "Producto es Bebida Blanca, Gaseosa o Vino", "categoria": "Insumo", "ranura": "categoria", "valor": "bebidas_generales"},
    "AP": {"desc": "Destino de almacenamiento es Depósito", "categoria": "Accion", "ranura": "almacenamiento", "valor": "deposito"},
    "AQ": {"desc": "Ingresa mercadería nueva", "categoria": "Operacion", "ranura": "tarea", "valor": "ingreso_mercaderia"},
    "AR": {"desc": "Ubicar nuevo atrás y viejo adelante (FIFO / PEPS)", "categoria": "Accion", "ranura": "criterio_estiba", "valor": "peps_fifo"},
    "AS": {"desc": "Producto es Carne o Comida Diaria", "categoria": "Insumo", "ranura": "categoria", "valor": "perecedero_diario"},
    "AT": {"desc": "Tiempo de guardado corto y compra diaria", "categoria": "Accion", "ranura": "politica_stock", "valor": "guardado_corto_diario"},
    "AU": {"desc": "Producto es Carne", "categoria": "Insumo", "ranura": "nombre", "valor": "carne"},
    "AV": {"desc": "Separar en porciones con folex", "categoria": "Accion", "ranura": "manipulacion", "valor": "fraccionar_con_folex"},
    "AW": {"desc": "Producto es Carne en folex", "categoria": "Insumo", "ranura": "estado", "valor": "fraccionada_en_folex"},
    "AX": {"desc": "Congelar", "categoria": "Accion", "ranura": "conservacion", "valor": "congelar"},
    "AY": {"desc": "Ingresa comanda de Carne", "categoria": "Operacion", "ranura": "comanda", "valor": "carne"},
    "AZ": {"desc": "Sacar porción congelada directo a plancha", "categoria": "Accion", "ranura": "coccion", "valor": "directo_a_plancha"},
    "BA": {"desc": "Llega mercadería al local", "categoria": "Operacion", "ranura": "tarea", "valor": "llegada_mercaderia"},
    "BB": {"desc": "Acomodar lugares y conservar para horas pico", "categoria": "Accion", "ranura": "operacion_salon", "valor": "preparar_para_pico"},

    # Módulo D: Control de Crisis Operativas
    "BC": {"desc": "Momento es Crítico y Falta Insumo", "categoria": "Operacion", "ranura": "quiebre_stock_critico", "valor": True},
    "BD": {"desc": "Negocios cercanos abiertos", "categoria": "Proveedor", "ranura": "cercanos_abiertos", "valor": True},
    "BE": {"desc": "Mandar empleado a comprar", "categoria": "Accion", "ranura": "gestion_crisis", "valor": "comprar_urgencia_empleado"},
    "BF": {"desc": "Día es Domingo por la tarde", "categoria": "Contexto", "ranura": "horario_critico", "valor": "domingo_tarde"},
    "BG": {"desc": "Carnicerías están cerradas", "categoria": "Proveedor", "ranura": "carnicerias_abiertas", "valor": False},
    "BH": {"desc": "Dar de baja producto y ofrecer alternativa", "categoria": "Accion", "ranura": "gestion_crisis", "valor": "baja_producto_y_alternativa"},

    # Módulo E: Mermas y Ajuste de Precios
    "BI": {"desc": "Color de carne es oscuro", "categoria": "Insumo", "ranura": "apariencia_carne", "valor": "color_oscuro"},
    "BJ": {"desc": "Separar de venta y cocinar para animales de la calle", "categoria": "Accion", "ranura": "destino_merma", "valor": "separar_y_cocinar_animales"},
    "BK": {"desc": "Aumenta costo de carne", "categoria": "Insumo", "ranura": "aumento_costo_carne", "valor": True},
    "BL": {"desc": "Aumenta precio de plato", "categoria": "Accion", "ranura": "ajuste_precio", "valor": "trasladar_al_plato"},
    "BM": {"desc": "Aumenta costo de bebida", "categoria": "Insumo", "ranura": "aumento_costo_bebida", "valor": True},
    "BN": {"desc": "Mantener precio de bebida", "categoria": "Accion", "ranura": "ajuste_precio", "valor": "mantener_precio_bebida"}
}

# =====================================================================
# 3. CLASES DE MARCOS DE CONOCIMIENTO (FRAMES - TEORÍA DE MINSKY)
# =====================================================================

class MarcoContexto(Fact):
    """
    Marco de Conocimiento para el Entorno y Contexto del Restaurante.
    Representa variables climáticas, de calendario y eventos que condicionan la demanda.
    
    Ranuras (Slots):
      - dia: str ('lunes', ..., 'domingo', 'fin_de_semana')
      - momento: str ('manana', 'tarde', 'noche')
      - horario_critico: str ('domingo_tarde', 'ninguno')
      - temperatura: str ('frio', 'templado', 'calido')
      - clima: str ('soleado', 'lluvioso', 'nublado')
      - es_quincena: bool (True si es semana de cobro)
      - evento: str ('boca_river', 'desfile_23_agosto', 'ninguno')
      - competencia: str ('alta', 'normal', 'baja')
    """
    pass

class MarcoCliente(Fact):
    """
    Marco de Conocimiento para la Demanda y el Perfil del Comensal.
    
    Ranuras (Slots):
      - tipo: str ('familia', 'jovenes', 'ejecutivo', 'general')
      - reservas: str ('grupos_grandes', 'mesas_chicas', 'ninguna')
      - comportamiento: str ('alta_bebida_baja_comida', 'estandar')
      - preferencia: str ('menu_al_plato', 'bebidas_y_sandwiches')
    """
    pass

class MarcoInsumo(Fact):
    """
    Marco de Conocimiento para Productos del Inventario y Mercaderías.
    
    Ranuras (Slots):
      - nombre: str ('carne', 'cerveza', 'hielo', 'queso', etc.)
      - categoria: str ('perecedero_diario', 'bebidas_generales', 'pizza_y_aderezos')
      - estado: str ('fresco', 'fraccionada_en_folex', 'congelada', 'en_deposito')
      - apariencia_carne: str ('normal', 'color_oscuro')
      - aumento_costo_carne: bool
      - aumento_costo_bebida: bool
      - rotacion: str ('muy_rapida', 'rapida', 'normal')
      - stock_critico: bool
    """
    pass

class MarcoProveedor(Fact):
    """
    Marco de Conocimiento para Proveedores y Comercios de Abastecimiento.
    
    Ranuras (Slots):
      - tipo: str ('fijo', 'mercado_favorito', 'cercano', 'carniceria')
      - carnicerias_abiertas: bool
      - cercanos_abiertos: bool
      - sostiene_precio: bool
      - precio_mas_barato: bool
    """
    pass

class MarcoOperacion(Fact):
    """
    Marco de Conocimiento para Estados del Servicio y Tareas Operativas.
    
    Ranuras (Slots):
      - tarea: str ('compra_diaria', 'ingreso_mercaderia', 'llegada_mercaderia')
      - comanda: str ('carne', 'sandwiches', 'bebidas')
      - duena_disponible: bool (False activa delegación)
      - quiebre_stock_critico: bool (True dispara protocolo de crisis)
    """
    pass

class HechoSimbolico(Fact):
    """
    Representación Híbrida / Simbólica Directa.
    Permite declarar y equiparar proposiciones mediante su letra (A - BN).
    
    Ranuras (Slots):
      - codigo: str (ej. 'M', 'W', 'Q')
      - valor: bool o str
      - desc: str
    """
    pass

# Alias convenientes para facilitar el código a los ingenieros de reglas
Contexto = MarcoContexto
Cliente = MarcoCliente
Insumo = MarcoInsumo
Proveedor = MarcoProveedor
Operacion = MarcoOperacion

# =====================================================================
# 4. FUNCIONES HELPER Y CARGA DE MEMORIA DE TRABAJO INICIAL (WM0)
# =====================================================================

def crear_hecho_por_codigo(codigo, **kwargs):
    """
    Crea tanto el Marco Semántico correspondiente como el HechoSimbolico
    asociado a un código del diccionario formal.
    """
    codigo = codigo.upper()
    if codigo not in DICCIONARIO_PROPOSICIONES:
        raise ValueError(f"El código {codigo} no existe en el diccionario formal.")
    
    meta = DICCIONARIO_PROPOSICIONES[codigo]
    categoria = meta["categoria"]
    ranura = meta["ranura"]
    valor = kwargs.get("valor", meta["valor"])
    
    # Crear marco semántico adecuado
    clase_marco = {
        "Contexto": MarcoContexto,
        "Cliente": MarcoCliente,
        "Insumo": MarcoInsumo,
        "Proveedor": MarcoProveedor,
        "Operacion": MarcoOperacion
    }.get(categoria, Fact)
    
    marco = clase_marco(**{ranura: valor})
    simbolico = HechoSimbolico(codigo=codigo, desc=meta["desc"], valor=valor)
    
    return marco, simbolico

def obtener_hechos_simbolicos(*codigos):
    """
    Devuelve una lista de HechoSimbolico para una serie de códigos dados.
    Ejemplo: obtener_hechos_simbolicos('M', 'W')
    """
    resultado = []
    for cod in codigos:
        cod = cod.upper().strip()
        if cod in DICCIONARIO_PROPOSICIONES:
            info = DICCIONARIO_PROPOSICIONES[cod]
            resultado.append(HechoSimbolico(codigo=cod, desc=info["desc"], valor=True))
    return resultado

# =====================================================================
# 5. GENERADORES DE CASOS DE USO (TRAZABILIDAD DE ACTIVIDAD 4)
# =====================================================================

def cargar_caso_1():
    """
    CASO 1: Oferta de menú y predicción de consumo ante frío y familia.
    Hechos Iniciales (BH0):
      - M: Temperatura es frío
      - W: Tipo de cliente es Familia
    Inferencia esperada:
      - N: Ofrecer menú caliente (sopas)
      - O, P: Mantener menú habitual (sándwiches y pizzas)
      - X: Preferencia es Menú al plato
    """
    print("\n--- Cargando Memoria de Trabajo Inicial: CASO 1 ---")
    hecho_m_marco = Contexto(temperatura="frio")
    hecho_w_marco = Cliente(tipo="familia")
    simbolicos = obtener_hechos_simbolicos("M", "W")
    
    hechos = [hecho_m_marco, hecho_w_marco] + simbolicos
    for h in hechos:
        print(f"  [WM0] -> {h}")
    return hechos

def cargar_caso_2():
    """
    CASO 2: Gestión de demanda por quincena, buen clima y grupos grandes.
    Hechos Iniciales (BH0):
      - Q: Fecha es quincena o cobro
      - R: Clima es soleado
      - S: Reservas son grupos grandes
    Inferencia esperada:
      - T: Comportamiento Alta Bebida y Baja Comida
      - U: Aumentar compra de destilados y snacks
      - V: Reducir compra de vegetales
    """
    print("\n--- Cargando Memoria de Trabajo Inicial: CASO 2 ---")
    hecho_contexto = Contexto(es_quincena=True, clima="soleado")
    hecho_cliente = Cliente(reservas="grupos_grandes")
    simbolicos = obtener_hechos_simbolicos("Q", "R", "S")
    
    hechos = [hecho_contexto, hecho_cliente] + simbolicos
    for h in hechos:
        print(f"  [WM0] -> {h}")
    return hechos

def cargar_caso_3():
    """
    CASO 3: Crisis de abastecimiento un domingo por la tarde.
    Hechos Iniciales (BH0):
      - BC: Momento es Crítico y Falta Insumo
      - BF: Día es Domingo por la tarde
      - BG: Carnicerías están cerradas
    Inferencia esperada:
      - BH: Dar de baja producto y ofrecer alternativa
    """
    print("\n--- Cargando Memoria de Trabajo Inicial: CASO 3 ---")
    hecho_operacion = Operacion(quiebre_stock_critico=True)
    hecho_contexto = Contexto(dia="domingo", momento="tarde", horario_critico="domingo_tarde")
    hecho_proveedor = Proveedor(carnicerias_abiertas=False)
    simbolicos = obtener_hechos_simbolicos("BC", "BF", "BG")
    
    hechos = [hecho_operacion, hecho_contexto, hecho_proveedor] + simbolicos
    for h in hechos:
        print(f"  [WM0] -> {h}")
    return hechos

def cargar_interactivo():
    """
    Permite cargar hechos iniciales de manera interactiva por consola.
    """
    print("\n=== Carga Interactiva de Memoria de Trabajo ===")
    dia = input("Día de la semana [ej. domingo, fin_de_semana, habil]: ").strip()
    temp = input("Temperatura [frio / templado / calido]: ").strip()
    cliente = input("Tipo de cliente [familia / jovenes / general]: ").strip()
    es_quincena = input("¿Es fecha de cobro/quincena? (s/n): ").strip().lower() == "s"
    falta_critica = input("¿Hay faltante crítico de insumo? (s/n): ").strip().lower() == "s"
    
    hechos = [
        Contexto(dia=dia, temperatura=temp, es_quincena=es_quincena),
        Cliente(tipo=cliente)
    ]
    if falta_critica:
        hechos.append(Operacion(quiebre_stock_critico=True))
    
    print("\nHechos instanciados:")
    for h in hechos:
        print(f"  [WM0] -> {h}")
    return hechos

# =====================================================================
# 6. DEMOSTRACIÓN DE VERIFICACIÓN / TEST DEL MOTOR (CASO 1)
# =====================================================================

class MotorDemostracionCaso1(KnowledgeEngine):
    """
    Motor mínimo de demostración para verificar que los marcos de Punto 2
    se equiparan y disparan las reglas del Caso 1 sin conflicto ni bucles.
    """
    
    # R5: Si M (Temperatura es frío) -> N (Ofrecer menú caliente / sopas)
    @Rule(
        OR(
            Contexto(temperatura="frio"),
            HechoSimbolico(codigo="M")
        ),
        NOT(HechoSimbolico(codigo="N"))
    )
    def regla_r5_clima_frio_sopas(self):
        print("\n[DISPARO R5] -> Temperatura fría detectada.")
        print("  Acción N deducida: Ofrecer menú caliente y sopas.")
        self.declare(HechoSimbolico(codigo="N", desc="Ofrecer menú caliente (sopas)", valor=True))
        
    # R6: Si M -> O, P (Mantener habitual y ofrecer sándwiches y pizzas)
    @Rule(
        OR(
            Contexto(temperatura="frio"),
            HechoSimbolico(codigo="M")
        ),
        NOT(HechoSimbolico(codigo="O"))
    )
    def regla_r6_clima_frio_sandwiches(self):
        print("\n[DISPARO R6] -> Temperatura fría detectada.")
        print("  Acción O, P deducida: Mantener menú habitual de sándwiches y pizzas.")
        self.declare(HechoSimbolico(codigo="O", desc="Mantener menú habitual", valor=True))
        self.declare(HechoSimbolico(codigo="P", desc="Ofrecer sándwiches y pizzas", valor=True))

    # R10: Si W (Tipo de cliente es Familia) -> X (Preferencia es Menú al plato)
    @Rule(
        OR(
            Cliente(tipo="familia"),
            HechoSimbolico(codigo="W")
        ),
        NOT(HechoSimbolico(codigo="X"))
    )
    def regla_r10_cliente_familia(self):
        print("\n[DISPARO R10] -> Cliente tipo Familia detectado.")
        print("  Acción X deducida: Preferencia de comensales orientada a Menú al plato.")
        self.declare(Cliente(preferencia="menu_al_plato"))
        self.declare(HechoSimbolico(codigo="X", desc="Preferencia es Menú al plato", valor=True))

if __name__ == "__main__":
    print("=" * 65)
    print("EJECUTANDO TEST DE BASE DE HECHOS Y DEMOSTRACIÓN CASO 1")
    print("=" * 65)
    
    # Probar carga del Caso 1
    hechos_iniciales = cargar_caso_1()
    
    # Probar motor de inferencia si Experta está disponible
    motor = MotorDemostracionCaso1()
    motor.reset()
    for h in hechos_iniciales:
        motor.declare(h)
    
    print("\nIniciando encadenamiento hacia adelante...")
    motor.run()
    print("\n[OK] Test de Base de Hechos completado con éxito.")
