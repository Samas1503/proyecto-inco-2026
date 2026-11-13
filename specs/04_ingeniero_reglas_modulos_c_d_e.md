# Especificación Técnica: Punto 4 – Ingeniero de Reglas Lógicas 2 (Módulos C, D y E)

## 👤 Rol
* **Rol:** Ingeniero de Reglas Lógicas 2
* **Entregable:** Módulo de reglas en Python (`reglas_modulos_c_d_e.py`) o celdas correspondientes en el Colab principal, programando las **Reglas 19 a 30** con la librería `experta`.

---

## 🎯 Alcance de Reglas a Implementar

Debes traducir estrictamente al decorador `@Rule` de `experta` las reglas formalizadas en `documentos_referencia/formalizacion_logica.txt`:

### Módulo C: Almacenamiento, Conservación y Flujo de Cocina
* **Regla 19:** $AO \implies AP$ (Bebida blanca/gaseosa/vino $\implies$ Almacenamiento en depósito).
* **Regla 20:** $AQ \implies AR$ (Ingresa mercadería nueva $\implies$ Criterio FIFO/PEPS: nuevo atrás, viejo adelante).
* **Regla 21:** $AS \implies AT$ (Carne o comida diaria $\implies$ Tiempo de guardado corto y compra diaria).
* **Regla 22:** $AU \implies AV$ (Carne fresca $\implies$ Separar en porciones individuales con folex).
* **Regla 23:** $AW \implies AX$ (Carne fraccionada en folex $\implies$ Congelar de inmediato).
* **Regla 24:** $AY \implies AZ$ (Comanda activa de carne $\implies$ Sacar porción congelada directo a la plancha).
* **Regla 25:** $BA \implies BB$ (Llega mercadería al local $\implies$ Acomodar lugares y conservar para horas pico).

### Módulo D: Operación en Servicio y Control de Crisis
* **Regla 26:** $BC \land BD \implies BE$ (Momento crítico + Falta insumo + Comercios cercanos abiertos $\implies$ Mandar empleado de urgencia a comprar).
* **Regla 27:** $BC \land BF \land BG \implies BH$ (Momento crítico + Domingo tarde + Carnicerías cerradas $\implies$ Dar de baja plato inmediatamente y ofrecer alternativa gastronómica).

### Módulo E: Control de Mermas y Ajuste de Precios (Facetas Procedimentales)
* **Regla 28:** $BI \implies BJ$ (Carne color oscuro detectada $\implies$ Separar de venta al público y cocinar para animales de la calle).
* **Regla 29:** $BK \implies BL$ (Aumenta costo de la carne $\implies$ Trasladar incremento al precio de venta del plato).
* **Regla 30:** $BM \implies BN$ (Aumenta costo de la bebida $\implies$ Mantener precio de venta de la bebida para fidelizar).

---

## 🛠️ Reglas de Programación Obligatorias
1. **Convención y Patrón de Referencia (Mitchell Blancas):**
   * Seguir las buenas prácticas demostradas en la clase del [Ing. Mitchell Blancas](https://youtu.be/wZz7ZKaEyGQ) para estructurar el motor de reglas en `experta`, enlazando hechos intermedios y evitando re-disparos cíclicos.
2. **Importación canónica:** Utilizar las clases de `marcos.py`:
   ```python
   from marcos import (
       Rule, KnowledgeEngine, Contexto, Cliente, Insumo,
       Proveedor, Operacion, HechoSimbolico, OR, AND
   )
   ```
2. **Facetas Procedimentales:** En las reglas 28 y 29, documentar en los comentarios cómo estas reglas actúan como facetas de reacción automática (*daemons*) ante cambios en los atributos del marco `Insumo`.

---

## 🛑 Protocolo Mandatorio `Grill-With-Me` para este Punto

Antes de programar las reglas, **la IA debe interrogarte** sobre:
1. *¿Cómo modelar el encadenamiento secuencial de la carne (R22 -> R23 -> R24) para que el estado pase de 'fresco' a 'en_folex' y luego a 'congelado'?*
2. *¿Qué prioridad o salience debe tener la Regla de Crisis R27 frente a la Regla R26?*
3. *¿Cómo se capturan los efectos de las facetas procedimentales de merma (R28) en la interfaz final?*
