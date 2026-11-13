# Especificación Técnica: Punto 5 – Desarrollador de Interfaz y Módulo de Explicación

## 👤 Rol
* **Rol:** Desarrollador de Interfaz de Usuario y Módulo de Explicación
* **Entregable Principal:** Finalización de la aplicación web en Streamlit ([`frontend/app.py`](../frontend/app.py)) conectada al motor de inferencia unificado, con visualización de la Memoria de Trabajo y Módulo de Explicación (*Explainability*).

---

## 📚 Documentación y Referencias de Implementación

1. **Clase Magistral de Mitchell Blancas:** [Sistema experto y SBC con Experta en Python](https://youtu.be/wZz7ZKaEyGQ).
   * Muestra cómo capturar los inputs del usuario, poblar la memoria de trabajo y mostrar las decisiones al usuario final.
2. **Guía Teórica de CLIPS (Universidad de Jaén):** [`documentos_referencia/clips_tutorial_ujaen.txt`](../documentos_referencia/clips_tutorial_ujaen.txt).
   * Emulación conceptual de las directivas de trazabilidad: `(watch facts)`, `(watch rules)` y visualización de la `(agenda)`.
3. **Estructura Base del Frontend ya Creada:** [`frontend/app.py`](../frontend/app.py).

---

## 🎯 Objetivos Específicos

### 1. Conexión del Frontend con el Motor Unificado
Debes instanciar la clase central del motor de inferencia que herede de `KnowledgeEngine` y combine los mixins de reglas programados por los Puntos 3 y 4:

```python
class MotorInferenciaCompleto(KnowledgeEngine, ModuloReglasABMixin, ModuloReglasCDEMixin):
    """Motor unificado del Sistema Experto Gastronómico."""
    pass
```

### 2. Implementación del Módulo de Explicación (Explainability)
Un Sistema Experto debe ser capaz de explicar **POR QUÉ** tomó una decisión ante el usuario o docente. Debes implementar un mecanismo para capturar la traza de reglas disparadas:
* Por cada disparo de regla:
  1. **Regla disparada:** Ej. `Regla R27 (Crisis de Domingo)`.
  2. **Premisas satisfechas:** `BC (Quiebre de stock crítico) ∧ BF (Domingo por la tarde) ∧ BG (Carnicerías cerradas)`.
  3. **Conclusión o Acción deducida:** `BH (Dar de baja plato y ofrecer alternativa gastronómica)`.
  4. **Justificación en lenguaje natural:** *"Se activó el protocolo de emergencia gastronómica porque no hay carnicerías abiertas en domingo tarde, garantizando la satisfacción del cliente sin interrumpir el servicio de salón."*

### 3. Visualización de la Memoria de Trabajo ($WM_0 \to WM_{final}$)
* Siguiendo el concepto de `(facts)` y `(watch facts)` del tutorial de Jaén, la UI debe mostrar:
  * **Estado Inicial ($WM_0$):** Lista de hechos introducidos por los selectores o cargados desde los casos de prueba.
  * **Estado Final ($WM_{final}$):** Hechos agregados tras el ciclo de encadenamiento hacia adelante.

---

## 🛑 Protocolo Mandatorio `Grill-With-Me` para este Punto

Antes de modificar el frontend con un asistente de IA, **el asistente debe interrogarte** sobre:
1. *¿Cómo interceptará Streamlit los prints o eventos de disparo del motor de Experta? (¿Capturando `sys.stdout` o guardando los eventos en una lista `self.explicaciones` dentro del motor?)*
2. *¿Deseas incorporar un visualizador gráfico del árbol de inferencia o tarjetas colapsables (`st.expander`) para cada decisión?*
3. *¿Qué estilo visual se utilizará para diferenciar alertas de crisis (rojo), sugerencias de compra (amarillo) y recomendaciones de menú (verde)?*
