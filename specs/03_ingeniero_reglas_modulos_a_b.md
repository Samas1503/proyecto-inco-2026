# Especificación Técnica: Punto 3 – Ingeniero de Reglas Lógicas 1 (Módulos A y B)

## 👤 Rol
* **Rol:** Ingeniero de Reglas Lógicas 1 (Núcleo Predictivo y de Compras)
* **Entregable:** Módulo de reglas en Python (`reglas_modulos_a_b.py`) o celdas correspondientes en el Colab principal, programando las **Reglas 1 a 18** con la librería `experta`.

---

## 📚 Documentación y Referencias de Implementación

1. **Clase Magistral de Mitchell Blancas:** [Sistema experto y SBC con Experta en Python](https://youtu.be/wZz7ZKaEyGQ).
   * Uso del decorador `@Rule`, captura de hechos con `AS` (`AS.f << Fact(...)`), emparejamiento con `MATCH`, aserción secuencial con `self.declare(...)`.
2. **Guía Teórica de CLIPS (Universidad de Jaén):** [`documentos_referencia/clips_tutorial_ujaen.txt`](../documentos_referencia/clips_tutorial_ujaen.txt).
   * Estructura de producción LHS $\implies$ RHS.
   * Regla de oro: No invocar reglas directamente; usar **hechos intermedios** para encadenamiento hacia adelante conducido por datos.
   * Prevención de bucles infinitos mediante patrones de no-existencia (`NOT`).
3. **Módulo Base de Hechos:** [`implementacion/marcos.py`](../implementacion/marcos.py).
   * Contiene los marcos: `Contexto`, `Cliente`, `Insumo`, `Proveedor`, `Operacion` y `HechoSimbolico`.

---

## 🎯 Reglas a Implementar (Módulos A y B)

### Módulo A: Predicción de Demanda y Oferta de Menú
* **Regla 1:** $A \lor B \implies C, D$
  * *Premisa:* Día es Fin de semana ($A$) o Día es Domingo ($B$).
  * *Conclusión:* Aumentar compra de mercadería ($C$) y Surtir para mañana, tarde y noche ($D$).
* **Regla 2:** $E \implies F$
  * *Premisa:* Evento es Partido Boca/River ($E$).
  * *Conclusión:* Planificar turnos temprano y tarde ($F$).
* **Regla 3:** $E \implies G, H$
  * *Premisa:* Evento es Partido Boca/River ($E$).
  * *Conclusión:* Comprar bebidas de forma gradual ($G$) y No comprar bebidas de golpe ($H$).
* **Regla 4:** $I \land J \implies K, L$
  * *Premisa:* Evento es Desfile 23 de Agosto ($I$) y Competencia es Alta ($J$).
  * *Conclusión:* Reducir expectativa de demanda ($K$) y Evitar sobrestock ($L$).
* **Regla 5:** $M \implies N$
  * *Premisa:* Temperatura es frío ($M$).
  * *Conclusión:* Ofrecer menú caliente / sopas ($N$).
* **Regla 6:** $M \implies O, P$
  * *Premisa:* Temperatura es frío ($M$).
  * *Conclusión:* Mantener menú habitual ($O$) y Ofrecer sándwiches y pizzas ($P$).
* **Regla 7:** $Q \land R \land S \implies T$
  * *Premisa:* Fecha es quincena ($Q$), Clima es soleado ($R$) y Reservas son grupos grandes ($S$).
  * *Conclusión:* Comportamiento es Alta Bebida y Baja Comida ($T$).
* **Regla 8:** $T \implies U$
  * *Premisa:* Comportamiento $T$ activo en la Memoria de Trabajo.
  * *Conclusión:* Aumentar compra de destilados y snacks ($U$).
* **Regla 9:** $T \implies V$
  * *Premisa:* Comportamiento $T$ activo en la Memoria de Trabajo.
  * *Conclusión:* Reducir compra de vegetales ($V$).
* **Regla 10:** $W \implies X$
  * *Premisa:* Tipo de cliente es Familia ($W$).
  * *Conclusión:* Preferencia es Menú al plato ($X$).
* **Regla 11:** $Y \implies Z$
  * *Premisa:* Tipo de cliente es Jóvenes ($Y$).
  * *Conclusión:* Preferencia es Bebidas y sándwiches ($Z$).

### Módulo B: Adquisición, Prioridades y Proveedores
* **Regla 12:** $AA \implies AB$ (Cerveza $\implies$ Prioridad alta y rotación muy rápida).
* **Regla 13:** $AC \implies AD$ (Pre-pizza/Queso/Jamón/Salsa $\implies$ Prioridad alta y rotación rápida).
* **Regla 14:** $AE \implies AF$ (Compra Diaria $\implies$ Desplazarse a mercados favoritos).
* **Regla 15:** $AE \implies AG$ (Compra Diaria $\implies$ Pagar con efectivo/transferencia/tarjeta).
* **Regla 16:** $AH \implies AI$ (Dueña no disponible $\implies$ Delegar compra a Encargada de caja).
* **Regla 17:** $AJ \lor AA \implies AK$ (Hielo o Cerveza $\implies$ Proveedores fijos).
* **Regla 18:** $AL \land AM \implies AN$ (Local favorito no sostiene precio y otro más barato $\implies$ Cambiar proveedor).

---

## 💻 Patrón de Codificación Canónico (Estilo Mitchell Blancas + CLIPS)

Para garantizar consistencia y evitar bucles infinitos, cada regla debe seguir este formato:

```python
from marcos import (
    Rule, KnowledgeEngine, Contexto, Cliente, Insumo,
    Proveedor, Operacion, HechoSimbolico, OR, AND, NOT, AS
)

class ModuloReglasABMixin:

    # Ejemplo Regla 5: R5 (M => N)
    @Rule(
        OR(
            Contexto(temperatura="frio"),
            HechoSimbolico(codigo="M")
        ),
        NOT(HechoSimbolico(codigo="N")), # Prevención de disparo infinito (Guía CLIPS)
        salience=10
    )
    def regla_05_temperatura_fria_menu_caliente(self):
        print(" [FIRE R5] -> Clima frío detectado. Aseverando acción N: Ofrecer sopas y menú caliente.")
        self.declare(HechoSimbolico(codigo="N", desc="Ofrecer menú caliente (sopas)", valor=True))

    # Ejemplo Regla 7: R7 (Q, R, S => T)
    @Rule(
        AND(
            OR(Contexto(es_quincena=True), HechoSimbolico(codigo="Q")),
            OR(Contexto(clima="soleado"), HechoSimbolico(codigo="R")),
            OR(Cliente(reservas="grupos_grandes"), HechoSimbolico(codigo="S"))
        ),
        NOT(HechoSimbolico(codigo="T")),
        salience=10
    )
    def regla_07_quincena_sol_grupos_consumo_bebida(self):
        print(" [FIRE R7] -> Quincena + Sol + Grupos Grandes. Deduciendo T: Alta Bebida / Baja Comida.")
        self.declare(Cliente(comportamiento="alta_bebida_baja_comida"))
        self.declare(HechoSimbolico(codigo="T", desc="Comportamiento Alta Bebida y Baja Comida", valor=True))

    # Ejemplo Regla 8: R8 (T => U) Encadenamiento Puro
    @Rule(
        OR(
            Cliente(comportamiento="alta_bebida_baja_comida"),
            HechoSimbolico(codigo="T")
        ),
        NOT(HechoSimbolico(codigo="U")),
        salience=9
    )
    def regla_08_aumentar_destilados_snacks(self):
        print(" [FIRE R8] -> Disparo encadenado desde T. Aseverando U: Comprar destilados y snacks.")
        self.declare(HechoSimbolico(codigo="U", desc="Aumentar compra de destilados y snacks", valor=True))
```

---

## 🛑 Protocolo Mandatorio `Grill-With-Me` para este Punto

Antes de permitir que la IA genere el código de las reglas, **el asistente debe interrogarte** sobre:
1. *¿Cómo asignaremos los niveles de `salience` para que R5 y R6 respeten la regla del mínimo subíndice documentada en el Caso 1 de la Actividad 4?*
2. *¿La disyunción de R1 ($A \lor B$) y R17 ($AJ \lor AA$) la programaremos como un único bloque `OR(...)` o como dos métodos separados según el consejo de estilo de CLIPS?*
3. *¿Deseas que cada regla capture la instancia del hecho disparador con `AS` para mostrar los valores en los prints de depuración?*
