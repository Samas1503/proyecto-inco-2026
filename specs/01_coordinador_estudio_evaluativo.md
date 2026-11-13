# Especificación Técnica: Punto 1 – Coordinador y Redactor Técnico (Estudio Evaluativo)

## 👤 Rol
* **Rol:** Coordinador General y Redactor Técnico del Proyecto
* **Entregable Principal:** 
  1. Capítulo del **"Estudio evaluativo de las herramientas candidatas"** (justificación teórica y comparativa de CLIPS, DROOLS, SWI-Prolog y Python + Experta).
  2. **Informe Final Consolidado** de la Actividad 5 en formato académico institucional (FI-UNJu), integrando las Actividades 1 a la 5.

---

## 📚 Documentación y Referencias Obligatorias

El desarrollo de esta sección debe fundamentarse estrictamente en:
1. **Tutorial de CLIPS (I) – Universidad de Jaén** (*Prof. Fernando Martínez Santiago*, archivado en [`documentos_referencia/clips_tutorial_ujaen.txt`](../documentos_referencia/clips_tutorial_ujaen.txt)).
2. **Clase Magistral de Experta en Python** (*Ing. Mitchell Blancas*, [Ver video en YouTube](https://youtu.be/wZz7ZKaEyGQ)).
3. **Diccionario de Formalización Lógica** ([`documentos_referencia/formalizacion_logica.txt`](../documentos_referencia/formalizacion_logica.txt)).

---

## 🎯 Objetivos y Contenido del Estudio Evaluativo

### 1. Tabla Comparativa Formal de Herramientas Candidatas
Debes incluir y justificar en el informe la siguiente matriz de evaluación técnica:

| Criterio de Evaluación | CLIPS (C / CLI) | DROOLS (Java) | SWI-Prolog (Lógico) | Python + Experta (Seleccionada) |
|---|---|---|---|---|
| **Paradigma Principal** | Sistema de Producción Puro | Motor de Reglas Empresarial | Programación Lógica Pura | Sistema Basado en Reglas / Objetos |
| **Encadenamiento Nativo** | Hacia Adelante (*Forward*) | Hacia Adelante (*Forward*) | Hacia Atrás (*Backward Chaining*) | **Hacia Adelante (*Forward Chaining*)** |
| **Algoritmo de Equiparación**| Rete | ReteOO / PHREAK | SLD Resolution (Unificación) | **Rete (Optimizado en Python)** |
| **Modelado de Marcos (*Frames*)**| Requiere `deftemplate` rígido | Clases Java / POJOs complejos | Cláusulas de Horn / Términos | **Clases orientadas a objetos (`Fact`)** |
| **Integración con UI (Streamlit)**| Compleja (vía wrappers en C) | Compleja (Servidor Web / JVM) | Media (vía PyProlog / sockets) | **Nativa e inmediata (100% Python)** |
| **Portabilidad (Google Colab)** | Requiere compilación de binarios | Requiere instalación de JDK | Requiere paquetes de sistema | **Instalación directa (`pip install experta`)** |
| **Curva de Aprendizaje** | Alta (Sintaxis LISP de los años 80) | Muy Alta (Enterprise / XML / DRL) | Media-Alta (Lógica formal) | **Baja-Media (Sintaxis limpia de Python)** |

---

### 2. Justificación Teórica del Descarte y Selección

* **Por qué se descartó SWI-Prolog:**
  * Prolog está diseñado intrínsecamente para el **encadenamiento hacia atrás (*goal-driven*)**, donde se parte de una meta o hipótesis y se busca verificarla recursivamente.
  * En cambio, la gestión de inventarios gastronómicos es un problema **conducido por datos (*data-driven*)**: el sistema recibe eventos ambientales (clima, día, comensales, quiebre de stock) y debe reaccionar infiriendo planes de acción hacia adelante. Emular encadenamiento hacia adelante en Prolog requiere metaprogramación compleja y poco legible.
* **Por qué se descartó DROOLS:**
  * DROOLS es una solución empresarial pesada pensada para arquitecturas bancarias y corporativas en Java. La sobrecarga de configuración de archivos `.drl`, integración de dependencias Maven/Gradle y consumo de memoria resulta desproporcionada y hostil para una entrega académica en Google Colab.
* **Por qué se descartó CLIPS (a pesar de compartir la misma teoría):**
  * Como documenta el *Tutorial de CLIPS de la Universidad de Jaén*, CLIPS utiliza una notación basada en LISP con archivos `.clp` (`defrule`, `assert`, `retract`). 
  * Si bien su motor Rete es la referencia histórica ideal, su falta de interoperabilidad con interfaces web modernas (Streamlit) y la imposibilidad de ejecutarlo directamente en Colab sin compilar binarios en C motivaron el salto a su equivalente moderno.
* **Por qué se seleccionó Python + Experta:**
  * Como demuestra el *Ing. Mitchell Blancas en su clase*, `experta` traslada fielmente toda la potencia de CLIPS al ecosistema Python. Mantiene las nociones de `Fact`, `@Rule`, `DefFacts`, `salience`, memoria de trabajo (`reset`) y disparo secuencial (`run`), pero con la ventaja de modelar **Marcos de Marvin Minsky** mediante clases nativas y conectarse en tiempo real a una interfaz gráfica web en Streamlit.

---

### 3. Tareas de Consolidación del Documento Final
1. **Unificación Estilística:** Consolidar en un único informe académico:
   * Actividad 1: Descripción del Dominio Gastronómico y Justificación de Insumos.
   * Actividad 2: Relevamiento y Transcripción de las Entrevistas al Experto.
   * Actividad 3: Análisis de Tareas y Diagramas de Flujo Operativos.
   * Actividad 4: Diccionario de 66 Proposiciones, 30 Reglas y Trazabilidad de los 3 Casos de Uso.
   * Actividad 5: Estudio Evaluativo de Herramientas, Arquitectura de Marcos (`marcos.py`), Código de Reglas y Frontend en Streamlit.
2. **Supervisión de Nomenclatura:** Verificar que los nombres de los hechos usados por los Ingenieros 1 y 2 coincidan con la formalización de la Actividad 4 sin discrepancias.

---

## 🛑 Protocolo Mandatorio `Grill-With-Me` para este Punto

Antes de redactar el texto final con cualquier asistente de IA, **el asistente debe interrogarte** sobre:
1. *¿Qué estructura de capítulos o índice exige la cátedra para la entrega final?*
2. *¿Desean incluir extractos de código CLIPS del tutorial de Jaén comparados lado a lado con el código Experta de Mitchell Blancas en una tabla visual?*
3. *¿Qué formato de citas bibliográficas prefiere el equipo docente (normas APA 7ma edición o estándar IEEE)?*
