# Especificación Técnica: Punto 5 – Desarrollador de Interfaz y Módulo de Explicación

## 👤 Rol
* **Rol:** Desarrollador de Interfaz de Usuario y Módulo de Explicación
* **Entregable:** Extensión y finalización de la aplicación web en Streamlit (`frontend/app.py`) conectada al motor de inferencia unificado, con trazabilidad visual y justificación de decisiones en pantalla.

---

## 🎯 Objetivos Específicos
1. **Conectar el Frontend con el Motor Unificado:**
   * Utilizar la base ya creada en [`frontend/app.py`](../frontend/app.py).
   * Instanciar el motor de inferencia que integrará las reglas del Punto 3 y Punto 4.
   * Permitir que el usuario/profesor interactúe mediante los selectores o cargue con un solo clic los **Casos 1, 2 y 3**.
2. **Programar el Módulo de Explicación (Explainability):**
   * En los Sistemas Expertos, el motor debe justificar **CÓMO** y **POR QUÉ** llegó a cada conclusión.
   * Por cada regla disparada, el sistema debe recolectar la traza de ejecución:
     * *Regla disparada:* Ej. `Regla 27`
     * *Premisas satisfechas:* Ej. `Momento crítico (BC) ∧ Domingo tarde (BF) ∧ Carnicerías cerradas (BG)`
     * *Acción resultante:* Ej. `Dar de baja producto y ofrecer alternativa gastronómica (BH)`
     * *Justificación en lenguaje natural:* Mensaje claro y comprensible para el comensal o personal de salón.
3. **Estilo y Presentación Visual:**
   * Organizar las conclusiones en tarjetas temáticas usando alertas y componentes visuales de Streamlit (`st.success`, `st.warning`, `st.error`, `st.info`).
   * Mostrar el estado antes y después de la Memoria de Trabajo ($WM_0 \to WM_{final}$).

---

## 🛑 Protocolo Mandatorio `Grill-With-Me` para este Punto

Antes de programar la UI y el módulo de explicación, **la IA debe interrogarte** sobre:
1. *¿Cómo interceptará el frontend los eventos de disparo del motor de Experta? (¿Vía decorador custom, escuchador de eventos o lista de hechos resultantes en el motor?)*
2. *¿Deseamos incluir una vista en árbol o gráfico de dependencias (por ejemplo con Graphviz o Mermaid) para visualizar la cadena de inferencias?*
3. *¿Cómo se manejará el despliegue de la app para la demostración en vivo con la cátedra (localhost vs Streamlit Community Cloud)?*
