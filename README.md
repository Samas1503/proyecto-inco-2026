# 🧠 Sistema Basado en Conocimiento: Optimización de Inventarios en el Sector Gastronómico
### Trabajo de Campo – Ingeniería del Conocimiento (InCo 2026)
**Facultad de Ingeniería – Universidad Nacional de Jujuy (FI-UNJu)**

---

## 👥 Grupo 02 – Integrantes
* **Carrizo, Shaira Maite** (DNI: 44326364)
* **Guari, Benjamin Gabriel** (DNI: 45108543)
* **Ortega, Franco Gabriel** (DNI: 45559826)
* **Paredes, Samuel Elias** (DNI: 44706400)
* **Pellisco, Dana Aylén** (DNI: 43698710)
* **Perez Apumaita Jonatan M. M** (DNI: 44754394)

---

## 📌 Descripción del Dominio y Problema
En el rubro gastronómico, la toma de decisiones sobre compras y control de stock no se resuelve con un cálculo lineal de entradas y salidas:
1. **Riesgo por falta de stock:** Quedarse sin ingredientes interrumpe el servicio y genera ventas perdidas.
2. **Riesgo por sobrestock:** Adquirir insumos perecederos de más ocasiona mermas y pérdidas económicas directas.

Este **Sistema Basado en Conocimiento (SBC)** modela la experiencia heurística del experto gastronómico a través de:
* Un motor de inferencia con **encadenamiento hacia adelante (forward chaining)**.
* Representación del conocimiento mediante **Marcos (*Frames*) de Marvin Minsky** (ranuras y facetas procedimentales).
* Un diccionario canónico formal de **66 proposiciones ($A$ a $BN$)**.

---

## 📂 Estructura del Repositorio

```text
├── frontend/
│   ├── app.py                               # Interfaz gráfica en Streamlit con Módulo de Explicación
│   ├── requirements.txt                     # Dependencias del frontend
│   └── README.md                            # Guía de ejecución del servidor Streamlit
│
├── specs/
│   ├── README.md                            # Guía maestra y Protocolo Mandatorio Grill-With-Me
│   ├── 01_coordinador_estudio_evaluativo.md # Especificación Punto 1
│   ├── 03_ingeniero_reglas_modulos_a_b.md   # Especificación Punto 3 (Reglas R1 a R18)
│   ├── 04_ingeniero_reglas_modulos_c_d_e.md # Especificación Punto 4 (Reglas R19 a R30)
│   ├── 05_desarrollador_frontend_explicacion.md # Especificación Punto 5 (UI y Explicación)
│   └── 06_qa_validador_casos.md             # Especificación Punto 6 (QA y Casos de Prueba)
│
├── implementacion/
│   ├── IC2026 - Trabajo de Campo - G2.ipynb   # Cuaderno interactivo central para Google Colab
│   ├── main.ipynb                           # Alias estándar del notebook principal
│   ├── Punto2_Arquitecto_Base_Hechos.ipynb   # Desarrollo modular del Punto 2 (Base de Hechos)
│   ├── marcos.py                            # Clases de Marcos en Python (Fact / Experta)
│   └── README.md                            # Documentación técnica de la implementación
│
└── documentos_referencia/
    ├── definicion_de_dominio.txt            # Planteo del problema y justificación del SBC
    ├── division_de_puntos.txt               # Roles y tareas asignadas al equipo
    ├── formalizacion_logica.txt             # Diccionario formal de 66 proposiciones y 30 reglas
    ├── planificacion_preguntas.txt          # Guía de educción para las entrevistas
    └── entrevista_inventario.txt            # Transcripción del relevamiento de tareas
```

---

## 🚀 Ejecución en Google Colab

Puedes abrir y ejecutar el cuaderno principal directamente en Google Colab:
1. Sube o abre [`implementacion/IC2026 - Trabajo de Campo - G2.ipynb`](implementacion/IC2026%20-%20Trabajo%20de%20Campo%20-%20G2.ipynb) en Colab.
2. La celda de inicio instala y aplica automáticamente el parche de compatibilidad para `experta` en Python 3.10+:
   ```python
   !pip install frozendict experta --quiet
   ```
3. Ejecuta las celdas secuencialmente para validar la carga de la **Memoria de Trabajo Inicial ($WM_0$)** y los casos de encadenamiento hacia adelante.

---

## 💻 Ejecución Local (Python)

Para probar la Base de Hechos y la demostración de inferencia desde consola:

```bash
cd implementacion
python3 marcos.py
```

El script cuenta con un *fallback* autónomo en Python puro, permitiendo que se ejecute y verifique la lógica incluso sin tener instalada la librería `experta`.

---

## 📚 Referencias Bibliográficas y Recursos de Estudio

1. **Mitchell Blancas:** *"Sistema experto y sistema basado en conocimiento - Parte 2 (Programación en Python con Experta)"*. [Ver en YouTube](https://youtu.be/wZz7ZKaEyGQ?si=5OfwrloG9d754lfM).
   * Referencia metodológica principal utilizada por el equipo para el diseño de la arquitectura del motor de inferencia, asignación de identificadores con `AS`, y encadenamiento hacia adelante.
2. **Minsky, Marvin (1974):** *"A Framework for Representing Knowledge"*. MIT-AI Laboratory Memo 306 (Teoría de Marcos / *Frames*).
3. **Cátedra InCo (2026):** Material y guías de Trabajos Prácticos 1 al 5, Facultad de Ingeniería – UNJu.

