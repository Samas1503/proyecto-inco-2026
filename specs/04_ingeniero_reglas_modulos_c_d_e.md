# Especificación Técnica: Punto 4 – Ingeniero de Reglas Lógicas 2 (Módulos C, D y E)

## 👤 Rol
* **Rol:** Ingeniero de Reglas Lógicas 2 (Núcleo Operativo, Control de Crisis y Mermas)
* **Entregable:** Módulo de reglas en Python (`reglas_modulos_c_d_e.py`) o celdas correspondientes en el Colab principal, programando las **Reglas 19 a 30** con la librería `experta`.

---

## 📚 Documentación y Referencias de Implementación

1. **Clase Magistral de Mitchell Blancas:** [Sistema experto y SBC con Experta en Python](https://youtu.be/wZz7ZKaEyGQ).
   * Manejo de variables con `MATCH`, asignación de identificadores de hechos con `AS`, y mutación/aserción en la Memoria de Trabajo.
2. **Guía Teórica de CLIPS (Universidad de Jaén):** [`documentos_referencia/clips_tutorial_ujaen.txt`](../documentos_referencia/clips_tutorial_ujaen.txt).
   * Encadenamiento secuencial reactivo sin llamadas directas entre funciones.
   * Eliminación o transición de estados intermedios.
3. **Módulo Base de Hechos:** [`implementacion/marcos.py`](../implementacion/marcos.py).
   * Contiene los marcos: `Insumo`, `Proveedor`, `Operacion`, `Contexto` y `HechoSimbolico`.

---

## 🎯 Reglas a Implementar (Módulos C, D y E)

### Módulo C: Almacenamiento, Conservación y Flujo de Cocina
* **Regla 19:** $AO \implies AP$
  * *Premisa:* Producto es Bebida Blanca, Gaseosa o Vino ($AO$).
  * *Conclusión:* Destino de almacenamiento es Depósito ($AP$).
* **Regla 20:** $AQ \implies AR$
  * *Premisa:* Ingresa mercadería nueva ($AQ$).
  * *Conclusión:* Criterio de estiba FIFO/PEPS: nuevo atrás, viejo adelante ($AR$).
* **Regla 21:** $AS \implies AT$
  * *Premisa:* Producto es Carne o Comida Diaria ($AS$).
  * *Conclusión:* Tiempo de guardado corto y compra diaria ($AT$).
* **Regla 22:** $AU \implies AV$
  * *Premisa:* Producto es Carne fresca ($AU$).
  * *Conclusión:* Separar en porciones individuales con folex ($AV$).
* **Regla 23:** $AW \implies AX$
  * *Premisa:* Producto es Carne en folex ($AW$).
  * *Conclusión:* Congelar de inmediato ($AX$).
* **Regla 24:** $AY \implies AZ$
  * *Premisa:* Ingresa comanda de Carne ($AY$).
  * *Conclusión:* Sacar porción congelada directo a la plancha ($AZ$).
* **Regla 25:** $BA \implies BB$
  * *Premisa:* Llega mercadería al local ($BA$).
  * *Conclusión:* Acomodar lugares y conservar para horas pico ($BB$).

### Módulo D: Operación en Servicio y Control de Crisis
* **Regla 26:** $BC \land BD \implies BE$
  * *Premisa:* Momento Crítico y Falta Insumo ($BC$) $\land$ Negocios cercanos abiertos ($BD$).
  * *Conclusión:* Mandar empleado de urgencia a comprar ($BE$).
* **Regla 27:** $BC \land BF \land BG \implies BH$ (Caso 3 Formal)
  * *Premisa:* Momento Crítico y Falta Insumo ($BC$) $\land$ Día es Domingo tarde ($BF$) $\land$ Carnicerías cerradas ($BG$).
  * *Conclusión:* Dar de baja plato inmediatamente y ofrecer alternativa gastronómica al cliente ($BH$).

### Módulo E: Control de Mermas y Ajuste de Precios (Facetas Procedimentales)
* **Regla 28:** $BI \implies BJ$
  * *Premisa:* Color de la carne es oscuro ($BI$).
  * *Conclusión:* Separar de la venta comercial y cocinar para animales de la calle ($BJ$).
  * *Faceta procedimentale:* Actúa como un *daemon* automático de seguridad bromatológica.
* **Regla 29:** $BK \implies BL$
  * *Premisa:* Aumenta costo de la carne ($BK$).
  * *Conclusión:* Trasladar incremento al precio de venta del plato ($BL$).
* **Regla 30:** $BM \implies BN$
  * *Premisa:* Aumenta costo de la bebida ($BM$).
  * *Conclusión:* Mantener precio de venta de la bebida para fidelizar comensales ($BN$).

---

## 💻 Patrón de Codificación Canónico (Estilo Mitchell Blancas + CLIPS)

```python
from marcos import (
    Rule, KnowledgeEngine, Contexto, Cliente, Insumo,
    Proveedor, Operacion, HechoSimbolico, OR, AND, NOT, AS
)

class ModuloReglasCDEMixin:

    # Transición operativa de la carne (R22 -> R23)
    @Rule(
        OR(
            Insumo(nombre="carne", estado="fresco"),
            HechoSimbolico(codigo="AU")
        ),
        NOT(HechoSimbolico(codigo="AV")),
        salience=10
    )
    def regla_22_porcionar_carne_folex(self):
        print(" [FIRE R22] -> Carne fresca detectada. Fraccionando en folex.")
        self.declare(HechoSimbolico(codigo="AV", desc="Separar en porciones con folex", valor=True))
        # Aseverar estado intermedio que encadena hacia R23
        self.declare(HechoSimbolico(codigo="AW", desc="Producto es Carne en folex", valor=True))

    @Rule(
        HechoSimbolico(codigo="AW"),
        NOT(HechoSimbolico(codigo="AX")),
        salience=9
    )
    def regla_23_congelar_carne_folex(self):
        print(" [FIRE R23] -> Carne en folex reconocida. Aseverando congelación.")
        self.declare(HechoSimbolico(codigo="AX", desc="Congelar carne", valor=True))

    # Regla 27: Protocolo de Crisis de Abastecimiento (Caso 3)
    @Rule(
        AND(
            OR(Operacion(quiebre_stock_critico=True), HechoSimbolico(codigo="BC")),
            OR(Contexto(horario_critico="domingo_tarde"), HechoSimbolico(codigo="BF")),
            OR(Proveedor(carnicerias_abiertas=False), HechoSimbolico(codigo="BG"))
        ),
        NOT(HechoSimbolico(codigo="BH")),
        salience=15 # Alta prioridad por ser regla de crisis operativa
    )
    def regla_27_crisis_domingo_baja_producto(self):
        print(" 🚨 [FIRE R27] -> CRISIS: Domingo tarde sin carnicerías abiertas.")
        print("    Decisión deducida BH: Dar de baja el plato y ofrecer alternativa de inmediato.")
        self.declare(HechoSimbolico(codigo="BH", desc="Dar de baja producto y ofrecer alternativa", valor=True))

    # Regla 28: Faceta procedimental de merma bromatológica
    @Rule(
        OR(
            Insumo(apariencia_carne="color_oscuro"),
            HechoSimbolico(codigo="BI")
        ),
        NOT(HechoSimbolico(codigo="BJ")),
        salience=20 # Máxima prioridad: inocuidad alimentaria
    )
    def regla_28_merma_carne_oscura(self):
        print(" ⚠️ [FIRE R28] -> ALERTA BROMATOLÓGICA: Carne con color oscuro detectada.")
        print("    Acción BJ: Separar de venta y cocinar para animales de la calle.")
        self.declare(HechoSimbolico(codigo="BJ", desc="Separar y cocinar para animales", valor=True))
```

---

## 🛑 Protocolo Mandatorio `Grill-With-Me` para este Punto

Antes de permitir que la IA genere el código de las reglas, **el asistente debe interrogarte** sobre:
1. *¿Qué nivel de salience numérico debe tener la Regla 27 de crisis frente a la Regla 26 de compra en comercios cercanos?*
2. *¿La transición de la carne fresca a folex y congelada debe usar `self.modify` sobre el marco `Insumo` o aseverar hechos intermedios (`AW`) según el estilo de CLIPS?*
3. *¿Cómo reflejaremos las decisiones comerciales de precios (R29 y R30) en el panel de resultados del frontend?*
