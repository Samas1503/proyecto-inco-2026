"""
Módulo de Reglas Lógicas: Módulos C, D y E
Trabajo de Campo - Inteligencia del Conocimiento (InCo 2026)
Punto 4: Ingeniero de Reglas Lógicas 2 (Desarrollado por Jonatan Perez Apumaita / Integrado al repo)

Implementa:
- Módulo C: Almacenamiento y Conservación (R19 a R25)
- Módulo D: Operación en Servicio y Control de Crisis (R26 y R27)
- Módulo E: Control de Mermas y Ajuste de Precios (R28 a R30)
"""

from marcos import (
    KnowledgeEngine, Rule, Fact, Contexto, Cliente, Insumo,
    Proveedor, Operacion, HechoSimbolico, OR, AND, NOT,
    cargar_caso_3
)

class MotorModulosCDE(KnowledgeEngine):
    """
    Motor de Inferencia para los Módulos C, D y E.
    Desarrollado por Jona (Punto 4).
    """

    # --- MÓDULO C: Almacenamiento y Conservación ---
    @Rule(OR(Insumo(categoria="bebidas_generales"), HechoSimbolico(codigo="AO")))
    def r19_almacenamiento_bebidas(self):
        self.declare(HechoSimbolico(codigo="AP", desc="Destino a Depósito", valor=True))
        print(" -> [R19] Almacenamiento: Bebidas enviadas a depósito.")

    @Rule(OR(Operacion(tarea="ingreso_mercaderia"), HechoSimbolico(codigo="AQ")))
    def r20_estiba_peps(self):
        self.declare(HechoSimbolico(codigo="AR", desc="Estiba PEPS", valor=True))
        print(" -> [R20] Estiba: Acomodando mercadería nueva atrás y vieja adelante.")

    @Rule(OR(Insumo(categoria="perecedero_diario"), HechoSimbolico(codigo="AS")))
    def r21_tiempo_guardado(self):
        self.declare(HechoSimbolico(codigo="AT", desc="Guardado corto", valor=True))
        print(" -> [R21] Stock: Tiempo de guardado corto y compra diaria.")

    @Rule(OR(Insumo(nombre="carne"), HechoSimbolico(codigo="AU")))
    def r22_fraccionar_carne(self):
        self.declare(HechoSimbolico(codigo="AV", desc="Fraccionar en folex", valor=True))
        print(" -> [R22] Carnicería: Separando en porciones con folex.")

    @Rule(OR(Insumo(estado="fraccionada_en_folex"), HechoSimbolico(codigo="AW")))
    def r23_congelar_carne(self):
        self.declare(HechoSimbolico(codigo="AX", desc="Congelar", valor=True))
        print(" -> [R23] Conservación: Congelar de inmediato.")

    @Rule(OR(Operacion(comanda="carne"), HechoSimbolico(codigo="AY")))
    def r24_coccion_carne(self):
        self.declare(HechoSimbolico(codigo="AZ", desc="Carne a la plancha", valor=True))
        print(" -> [R24] Cocina: Sacar porción congelada directo a la plancha.")

    @Rule(OR(Operacion(tarea="llegada_mercaderia"), HechoSimbolico(codigo="BA")))
    def r25_acomodar_salon(self):
        self.declare(HechoSimbolico(codigo="BB", desc="Conservar horas pico", valor=True))
        print(" -> [R25] Salón: Acomodar lugares y conservar para horas pico.")

    # --- MÓDULO D: Operación en Servicio (Crisis y Faltantes) ---
    @Rule(AND(
        OR(Operacion(quiebre_stock_critico=True), HechoSimbolico(codigo="BC")),
        OR(Proveedor(cercanos_abiertos=True), HechoSimbolico(codigo="BD")),
        NOT(HechoSimbolico(codigo="BE"))
    ))
    def r26_comprar_urgencia(self):
        self.declare(HechoSimbolico(codigo="BE", desc="Compra de urgencia", valor=True))
        print(" -> [R26] Crisis: Mandando empleado a comprar urgente a comercio cercano.")

    @Rule(AND(
        OR(Operacion(quiebre_stock_critico=True), HechoSimbolico(codigo="BC")),
        OR(Contexto(horario_critico="domingo_tarde"), HechoSimbolico(codigo="BF")),
        OR(Proveedor(carnicerias_abiertas=False), HechoSimbolico(codigo="BG")),
        NOT(HechoSimbolico(codigo="BH")) # Condición antirrecursión
    ))
    def r27_baja_producto(self):
        self.declare(HechoSimbolico(codigo="BH", desc="Baja de producto", valor=True))
        print(" -> [R27] Crisis: Carnicerías cerradas. Dar de baja el producto y ofrecer alternativa.")

    # --- MÓDULO E: Control de Mermas y Ajuste de Precios ---
    @Rule(
        OR(Insumo(apariencia_carne="color_oscuro"), HechoSimbolico(codigo="BI")),
        NOT(HechoSimbolico(codigo="BJ"))
    )
    def r28_merma_carne(self):
        self.declare(HechoSimbolico(codigo="BJ", desc="Separar venta", valor=True))
        print(" -> [R28] Merma: Carne oscura separada para cocinar a animales de la calle.")

    @Rule(
        OR(Insumo(aumento_costo_carne=True), HechoSimbolico(codigo="BK")),
        NOT(HechoSimbolico(codigo="BL"))
    )
    def r29_aumento_plato(self):
        self.declare(HechoSimbolico(codigo="BL", desc="Aumento de plato", valor=True))
        print(" -> [R29] Precios: Aumenta costo de carne, trasladar incremento al plato.")

    @Rule(
        OR(Insumo(aumento_costo_bebida=True), HechoSimbolico(codigo="BM")),
        NOT(HechoSimbolico(codigo="BN"))
    )
    def r30_mantiene_bebida(self):
        self.declare(HechoSimbolico(codigo="BN", desc="Mantener bebida", valor=True))
        print(" -> [R30] Precios: Aumenta costo de bebida, mantener precio de venta.")

if __name__ == "__main__":
    print("\n--- TEST DE INTEGRACIÓN: MÓDULOS C, D y E con CASO 3 ---")
    motor_jona = MotorModulosCDE()
    motor_jona.reset()

    hechos_caso3 = cargar_caso_3()
    for hecho in hechos_caso3:
        motor_jona.declare(hecho)

    print("\n🚀 Ejecutando el motor para el Caso 3 (Forward Chaining)...\n")
    motor_jona.run()
    print("\n🏁 Fin de la ejecución de los módulos C, D y E.")
