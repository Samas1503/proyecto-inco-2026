# Especificación Técnica: Punto 1 – Coordinador y Redactor Técnico (Estudio Evaluativo)

## 👤 Rol
* **Rol:** Coordinador General y Redactor Técnico
* **Entregable:** Sección del "Estudio evaluativo de las herramientas candidatas" y consolidación del informe final de la Actividad 5 con formato académico.

---

## 🎯 Objetivos Específicos
1. **Redactar el Estudio Evaluativo de Herramientas Candidatas:**
   * Comparar teóricamente las herramientas tradicionales de Sistemas Basados en Conocimiento: **CLIPS**, **DROOLS**, **SWI-Prolog** frente a **Python + Experta**.
   * Justificar rigurosamente por qué se descartaron las demás en favor de Python con Experta:
     * **CLIPS:** Excelente para encadenamiento hacia adelante con el algoritmo Rete, pero sintaxis estilo LISP basada en archivos `.clp` (`defrule`, `assert`, `retract`) que dificulta la integración con interfaces web modernas (Streamlit), requeriría bindings externos en C (`clipsmm` o `pyclips`) y carece de portabilidad nativa en Google Colab.
       * *Referencia CLIPS:* Material docente de la Universidad de Jaén (*Tutorial de CLIPS - Prof. Fernando Martínez Santiago*, archivado en `documentos_referencia/clips_tutorial_ujaen.txt`).
     * **DROOLS:** Basado en Java, alta sobrecarga de configuración empresarial, innecesariamente complejo para el alcance del dominio gastronómico del local.
     * **SWI-Prolog:** Paradigma lógico puro con encadenamiento hacia atrás (*backward chaining*) nativo; requeriría metaprogramación compleja para emular el encadenamiento hacia adelante impulsado por datos (*data-driven*) que exige la planificación de inventarios.
     * **Python + Experta:** Encadenamiento hacia adelante nativo (algoritmo Rete simplificado), integración fluida con Streamlit, sintaxis limpia orientada a objetos (Marcos de Minsky) y portabilidad inmediata en Google Colab.
2. **Consolidar el Informe Final:**
   * Unificar las Actividades 1 a 4 con la Actividad 5 (implementación en código, interfaz y validación).
   * Supervisar que el código final programado por los Ingenieros 1 y 2 refleje exactamente la tabla de formalización lógica sin inventar nombres ni cambiar la semántica.
   * **Referencia Metodológica Obligatoria:** Citar e incorporar en el marco teórico y bibliográfico la clase magistral del **Ing. Mitchell Blancas**: *"Sistema experto y sistema basado en conocimiento - Parte 2 (Implementación de Experta en Python)"* (URL: https://youtu.be/wZz7ZKaEyGQ).

---

## 🛑 Protocolo Mandatorio `Grill-With-Me` para este Punto

Antes de permitir que la IA redacte el estudio comparativo, **la IA debe interrogarte** sobre:
1. *¿Qué estructura de rúbrica o criterios de comparación priorizará la cátedra? (Facilidad de integración, curva de aprendizaje, paradigma de encadenamiento, soporte multiplataforma).*
2. *¿Cuál es el formato final exigido por los docentes para el informe? (IEEE, APA, plantilla estándar de la cátedra de InCo FI-UNJu).*
3. *¿Cómo se integrarán los diagramas de flujo y las tablas de trazabilidad en el documento consolidado?*
