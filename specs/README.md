# 📋 Guía Maestra de Especificaciones (SPECS) para el Equipo
### Trabajo de Campo – Inteligencia del Conocimiento (InCo 2026)
**Grupo 02 – FI-UNJu**

Este directorio contiene las especificaciones técnicas individuales para cada integrante del equipo, garantizando que todo el código y la documentación se integren de forma cohesiva sobre la arquitectura base ya desarrollada en el [**Punto 2 (`implementacion/marcos.py`)**](../implementacion/marcos.py).

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
Es mandatorio que te bases 100% en el archivo de marcos ya desarrollado en el repositorio (implementacion/marcos.py) y en el diccionario formal de 66 proposiciones (documentos_referencia/formalizacion_logica.txt).
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
* **Estructura del Frontend:** [`frontend/app.py`](../frontend/app.py)
