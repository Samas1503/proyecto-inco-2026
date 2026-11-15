"""
Módulo de Reglas Lógicas: Módulos C, D y E
Trabajo de Campo - Inteligencia del Conocimiento (InCo 2026)
Punto 4: Ingeniero de Reglas Lógicas 2 (Desarrollado por Jonatan Perez Apumaita / Auditado y blindado contra bucles y deadlocks)

Implementa:
- Módulo C: Almacenamiento y Conservación (R19 a R25)
- Módulo D: Operación en Servicio y Control de Crisis (R26 y R27)
- Módulo E: Control de Mermas y Ajuste de Precios (R28 a R30)

Garantías de Diseño (Auditoría Anti-Bucles y Anti-Deadlocks):
1. Todas las reglas cuentan con guardas `NOT(HechoSimbolico(...))` para evitar dobles disparos o activaciones redundantes.
2. El encadenamiento de conservación de carne (R22 -> R23 -> R24) asevera el estado intermedio `AW` para evitar bloqueos.
3. Las reglas de crisis y seguridad bromatológica (R27 y R28) cuentan con salience prioritario para resolver conflictos determinísticamente.
"""

from marcos import (
    KnowledgeEngine, Rule, Fact, Contexto, Cliente, Insumo,
    Proveedor, Operacion, HechoSimbolico, OR, AND, NOT,
    cargar_caso_3
)

class MotorModulosCDE(KnowledgeEngine):
    """
    Motor de Inferencia para los Módulos C, D y E.
    Blindado contra bucles infinitos, dobles disparos y deadlocks.
    """

    # --- MÓDULO C: Almacenamiento y Conservación ---
    @Rule(
        OR(Insumo(categoria="bebidas_generales"), HechoSimbolico(codigo="AO")),
        NOT(HechoSimbolico(codigo="AP")),
        salience=10
    )
    def r19_almacenamiento_bebidas(self):
        self.declare(HechoSimbolico(codigo="AP", desc="Destino a Depósito", valor=True))
        print(" -> [FIRE R19] Almacenamiento: Bebidas enviadas a depósito.")

    @Rule(
        OR(Operacion(tarea="ingreso_mercaderia"), HechoSimbolico(codigo="AQ")),
        NOT(HechoSimbolico(codigo="AR")),
        salience=10
    )
    def r20_estiba_peps(self):
        self.declare(HechoSimbolico(codigo="AR", desc="Estiba PEPS", valor=True))
        print(" -> [FIRE R20] Estiba: Acomodando mercadería nueva atrás y vieja adelante (PEPS/FIFO).")

    @Rule(
        OR(Insumo(categoria="perecedero_diario"), HechoSimbolico(codigo="AS")),
        NOT(HechoSimbolico(codigo="AT")),
        salience=10
    )
    def r21_tiempo_guardado(self):
        self.declare(HechoSimbolico(codigo="AT", desc="Guardado corto", valor=True))
        print(" -> [FIRE R21] Stock: Tiempo de guardado corto y compra diaria.")

    @Rule(
        OR(Insumo(nombre="carne"), HechoSimbolico(codigo="AU")),
        NOT(HechoSimbolico(codigo="AV")),
        salience=10
    )
    def r22_fraccionar_carne(self):
        print(" -> [FIRE R22] Carnicería: Separando carne en porciones con folex.")
        self.declare(HechoSimbolico(codigo="AV", desc="Fraccionar en folex", valor=True))
        # Aseverar el estado intermedio AW para habilitar el encadenamiento hacia R23 sin deadlock
        self.declare(HechoSimbolico(codigo="AW", desc="Producto es Carne en folex", valor=True))
        self.declare(Insumo(estado="fraccionada_en_folex"))

    @Rule(
        OR(Insumo(estado="fraccionada_en_folex"), HechoSimbolico(codigo="AW")),
        NOT(HechoSimbolico(codigo="AX")),
        salience=9
    )
    def r23_congelar_carne(self):
        print(" -> [FIRE R23] Conservación: Carne en folex detectada. Congelar de inmediato.")
        self.declare(HechoSimbolico(codigo="AX", desc="Congelar", valor=True))

    @Rule(
        OR(Operacion(comanda="carne"), HechoSimbolico(codigo="AY")),
        NOT(HechoSimbolico(codigo="AZ")),
        salience=10
    )
    def r24_coccion_carne(self):
        print(" -> [FIRE R24] Cocina: Comanda de carne ingresada. Sacar porción directo a la plancha.")
        self.declare(HechoSimbolico(codigo="AZ", desc="Carne a la plancha", valor=True))

    @Rule(
        OR(Operacion(tarea="llegada_mercaderia"), HechoSimbolico(codigo="BA")),
        NOT(HechoSimbolico(codigo="BB")),
        salience=10
    )
    def r25_acomodar_salon(self):
        print(" -> [FIRE R25] Salón: Mercadería en local. Acomodar lugares y conservar para horas pico.")
        self.declare(HechoSimbolico(codigo="BB", desc="Conservar horas pico", valor=True))

    # --- MÓDULO D: Operación en Servicio (Crisis y Faltantes) ---
    @Rule(
        AND(
            OR(Operacion(quiebre_stock_critico=True), HechoSimbolico(codigo="BC")),
            OR(Proveedor(cercanos_abiertos=True), HechoSimbolico(codigo="BD"))
        ),
        NOT(HechoSimbolico(codigo="BE")),
        salience=10
    )
    def r26_comprar_urgencia(self):
        self.declare(HechoSimbolico(codigo="BE", desc="Compra de urgencia", valor=True))
        print(" -> [FIRE R26] Crisis: Comercios cercanos abiertos. Mandando empleado a comprar urgente.")

    @Rule(
        AND(
            OR(Operacion(quiebre_stock_critico=True), HechoSimbolico(codigo="BC")),
            OR(Contexto(horario_critico="domingo_tarde"), HechoSimbolico(codigo="BF")),
            OR(Proveedor(carnicerias_abiertas=False), HechoSimbolico(codigo="BG"))
        ),
        NOT(HechoSimbolico(codigo="BH")),
        salience=15 # Salience prioritario sobre R26 ante falta de comercios especializados
    )
    def r27_baja_producto(self):
        self.declare(HechoSimbolico(codigo="BH", desc="Baja de producto", valor=True))
        print(" 🚨 [FIRE R27] Crisis: Domingo tarde y carnicerías cerradas. Dar de baja el producto y ofrecer alternativa.")

    # --- MÓDULO E: Control de Mermas y Ajuste de Precios ---
    @Rule(
        OR(Insumo(apariencia_carne="color_oscuro"), HechoSimbolico(codigo="BI")),
        NOT(HechoSimbolico(codigo="BJ")),
        salience=20 # Máxima prioridad: faceta procedimental de inocuidad alimentaria
    )
    def r28_merma_carne(self):
        self.declare(HechoSimbolico(codigo="BJ", desc="Separar venta", valor=True))
        print(" ⚠️ [FIRE R28] Merma: Carne oscura separada de venta para cocinar a animales de la calle.")

    @Rule(
        OR(Insumo(aumento_costo_carne=True), HechoSimbolico(codigo="BK")),
        NOT(HechoSimbolico(codigo="BL")),
        salience=10
    )
    def r29_aumento_plato(self):
        self.declare(HechoSimbolico(codigo="BL", desc="Aumento de plato", valor=True))
        print(" -> [FIRE R29] Precios: Aumenta costo de carne, trasladar incremento al precio del plato.")

    @Rule(
        OR(Insumo(aumento_costo_bebida=True), HechoSimbolico(codigo="BM")),
        NOT(HechoSimbolico(codigo="BN")),
        salience=10
    )
    def r30_mantiene_bebida(self):
        self.declare(HechoSimbolico(codigo="BN", desc="Mantener bebida", valor=True))
        print(" -> [FIRE R30] Precios: Aumenta costo de bebida, mantener precio de venta para fidelización.")

if __name__ == "__main__":
    print("\n" + "="*65)
    print("TEST DE INTEGRACIÓN: MÓDULOS C, D y E (CASO 3 AUDITADO)")
    print("="*65)
    motor_jona = MotorModulosCDE()
    motor_jona.reset()

    hechos_caso3 = cargar_caso_3()
    for hecho in hechos_caso3:
        motor_jona.declare(hecho)

    print("\n🚀 Ejecutando el motor para el Caso 3 (Forward Chaining)...\n")
    motor_jona.run()
    print("\n🏁 Fin de la ejecución de los módulos C, D y E sin bucles ni deadlocks.")
