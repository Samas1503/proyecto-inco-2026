# 📋 Guía Maestra de Especificaciones (SPECS) para el Equipo
### Trabajo de Campo – Inteligencia del Conocimiento (InCo 2026)
**Grupo 02 – FI-UNJu**

Este directorio contiene las especificaciones técnicas individuales para cada integrante del equipo, garantizando que todo el código y la documentación se integren de forma rigurosa y cohesiva sobre la arquitectura base ya desarrollada en el [**Punto 2 (`implementacion/marcos.py`)**](../implementacion/marcos.py).

---

## 🏛️ Los Dos Pilares Metodológicos Oficiales del Proyecto

Todas las especificaciones y desarrollos técnicos del equipo se basan formalmente en:

1. **La Clase Magistral del Ing. Mitchell Blancas:** [Sistema experto y SBC con Experta en Python](https://youtu.be/wZz7ZKaEyGQ).
   * Define la sintaxis canónica en Python: herencia de `Fact`, métodos `@Rule`, captura de hechos con `AS`, emparejamiento con `MATCH`, aserción reactiva con `self.declare(...)` y el ciclo de vida del motor (`reset`, `run`).
2. **El Tutorial de CLIPS (I) de la Universidad de Jaén:** [`documentos_referencia/clips_tutorial_ujaen.txt`](../documentos_referencia/clips_tutorial_ujaen.txt) (*Prof. Fernando Martínez Santiago*).
   * Establece las directivas fundamentales de los Sistemas de Producción:
     * El encadenamiento hacia adelante debe ser **100% reactivo (*data-driven*)**, basado en hechos intermedios y nunca llamando una regla desde otra.
     * Prevención de bucles infinitos con patrones de no-existencia (`NOT`).
     * Trazabilidad de la Agenda y resolución del conjunto de conflicto emulando las directivas `(watch facts)` y `(watch rules)`.

---

## 🚨 REGLA DE ORO OBLIGATORIA: Uso de la Metodología `Grill-With-Me`

> ### ⚠️ PROTOCOLO ANTIALUCINACIÓN DE INTELIGENCIA ARTIFICIAL
> Si utilizas asistentes de Inteligencia Artificial (ChatGPT, Claude, Gemini, Antigravity, GitHub Copilot) para desarrollar tu parte, **ESTÁ ESTRICTAMENTE PROHIBIDO pedirle que genere código o texto directamente en su primera respuesta**.
> 
> Los modelos de IA tienden a "alucinar" estructuras inventadas, nombres de variables inexistentes o sintaxis incompatibles con `experta`.
> 
> **Cada integrante DEBE iniciar su conversación con la IA pegando el siguiente Prompt de Activación Grill-Me:**

```text
Actúa como un Auditor Técnico Estricto y Arquitecto Senior en Sistemas Basados en Conocimiento.
Voy a desarrollar mi consigna asignada para el Trabajo de Campo de Inteligencia del Conocimiento (InCo 2026, FI-UNJu).

REGLA CRÍTICA:
No generes código ni soluciones completas de inmediato.
Activa el modo "grill-with-me": primero analiza mi consigna, lee la especificación y hazme un cuestionario interactivo con preguntas de decisión de diseño (con opciones recomendadas) para alinear y validar cada detalle técnico antes de escribir una sola línea de código.

Es mandatorio que te bases 100% en:
1. El archivo de marcos ya desarrollado en el repositorio (implementacion/marcos.py).
2. El diccionario formal de 66 proposiciones (documentos_referencia/formalizacion_logica.txt).
3. Los patrones canónicos de Python Experta demostrados por Mitchell Blancas (video https://youtu.be/wZz7ZKaEyGQ).
4. Las reglas de diseño de Sistemas de Producción del tutorial de CLIPS de la Universidad de Jaén (documentos_referencia/clips_tutorial_ujaen.txt).
```

---

## 🗺️ Mapa de Especificaciones por Rol

| Archivo de Especificación | Rol Asignado | Alcance Principal |
|---|---|---|
| [**`01_coordinador_estudio_evaluativo.md`**](01_coordinador_estudio_evaluativo.md) | Coordinador y Redactor Técnico | Justificación teórica de Experta vs CLIPS/DROOLS/Prolog + Consolidación del informe final. |
| [**`03_ingeniero_reglas_modulos_a_b.md`**](03_ingeniero_reglas_modulos_a_b.md) | Ingeniero de Reglas 1 | Reglas R1 a R18 (Módulo A: Demanda y Menú / Módulo B: Compras y Prioridades). |
| [**`04_ingeniero_reglas_modulos_c_d_e.md`**](04_ingeniero_reglas_modulos_c_d_e.md) | Ingeniero de Reglas 2 | Reglas R19 a R30 (Módulo C: Almacenamiento / Módulo D: Crisis / Módulo E: Mermas). |
| [**`05_desarrollador_frontend_explicacion.md`**](05_desarrollador_frontend_explicacion.md) | Desarrollador de Frontend | Completar `frontend/app.py` en Streamlit y programar el Módulo de Explicación. |
| [**`06_qa_validador_casos.md`**](06_qa_validador_casos.md) | Analista QA y Validador | Pruebas de encadenamiento hacia adelante de los Casos 1, 2 y 3, salience y ciclos. |

---

## 🔗 Recursos Base Compartidos
* **Marcos y Base de Hechos:** [`implementacion/marcos.py`](../implementacion/marcos.py)
* **Cuaderno Central:** [`implementacion/IC2026 - Trabajo de Campo - G2.ipynb`](../implementacion/IC2026%20-%20Trabajo%20de%20Campo%20-%20G2.ipynb)
* **Diccionario de 66 Proposiciones y Reglas:** [`documentos_referencia/formalizacion_logica.txt`](../documentos_referencia/formalizacion_logica.txt)
* **Tutorial de CLIPS UJaén:** [`documentos_referencia/clips_tutorial_ujaen.txt`](../documentos_referencia/clips_tutorial_ujaen.txt)
* **Estructura del Frontend:** [`frontend/app.py`](../frontend/app.py)
