# 🧠 Sistema Basado en Conocimiento: Optimización de Inventarios en Gastronomía
### Trabajo de Campo – Inteligencia del Conocimiento (InCo 2026)
**Facultad de Ingeniería – Universidad Nacional de Jujuy (FI-UNJu)**

[![Python 3.9+](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue.svg)](https://www.python.org/)
[![Experta](https://img.shields.io/badge/engine-Experta%20(Rete)-orange.svg)](https://github.com/nilp0inter/experta)
[![Streamlit](https://img.shields.io/badge/frontend-Streamlit-red.svg)](https://streamlit.io/)
[![Google Colab](https://img.shields.io/badge/Colab-Open%20Notebook-yellow.svg)](https://colab.research.google.com/github/Samas1503/proyecto-inco-2026/blob/main/implementacion/IC2026%20-%20Trabajo%20de%20Campo%20-%20G2.ipynb)

---

## 👥 Grupo 02 – Integrantes
* **Carrizo, Shaira Maite** (DNI: 44326364) – `44326364@fi.unju.edu.ar`
* **Guari, Benjamin Gabriel** (DNI: 45108543) – `45108543@fi.unju.edu.ar`
* **Ortega, Franco Gabriel** (DNI: 45559826) – `45559826@fi.unju.edu.ar`
* **Paredes, Samuel Elias** (DNI: 44706400) – `44706400@fi.unju.edu.ar` *(Punto 2: Arquitecto de Base de Hechos)*
* **Pellisco, Dana Aylén** (DNI: 43698710) – `pelliscodana.12@gmail.com`
* **Perez Apumaita Jonatan M. M** (DNI: 44754394) – `44754394@fi.unju.edu.ar` *(Punto 4: Reglas C, D y E)*

---

## 📌 Resumen del Dominio y del Sistema Experto

En el sector gastronómico, las decisiones sobre compras y control de stock no se resuelven con un cálculo lineal de entradas y salidas:
1. **Riesgo por falta de stock:** Quedarse sin insumos clave interrumpe el servicio de salón y genera ventas perdidas.
2. **Riesgo por sobrestock:** Adquirir insumos perecederos de más genera desperdicios económicos (mermas bromatológicas).

Este **Sistema Basado en Conocimiento (SBC)** captura y automatiza las heurísticas del encargado gastronómico mediante:
* Un motor de inferencia con **Encadenamiento Hacia Adelante (*Forward Chaining*)** basado en el algoritmo **Rete**.
* Representación del conocimiento mediante **Marcos (*Frames*) de Marvin Minsky** enriquecidos con ranuras y facetas procedimentales.
* Un diccionario canónico formal de **66 proposiciones ($A$ a $BN$)** y **30 reglas de producción**.
* Blindaje formal contra bucles infinitos y deadlocks mediante **guardas `NOT`** y calibración de prioridades (**`salience`**).

---

## 📚 Documentación Técnica Detallada (`docs/` y `GLOSARY.md`)

Para profundizar en el diseño e ingeniería del proyecto, consulta los documentos de soporte:

* 📖 [**`GLOSARY.md` (Glosario Técnico y Diccionario de 66 Proposiciones)**](GLOSARY.md): Definición canónica de términos de IA, Sistemas de Producción, variables del restaurante y el mapeo $A \dots BN$.
* 🏛️ [**`docs/01_arquitectura_del_sistema.md`**](docs/01_arquitectura_del_sistema.md): Arquitectura conceptual del SBC, red Rete y flujo de datos.
* 🧱 [**`docs/02_modelo_de_marcos.md`**](docs/02_modelo_de_marcos.md): Estructura detallada de las clases `MarcoContexto`, `MarcoCliente`, `MarcoInsumo`, `MarcoProveedor` y `MarcoOperacion`.
* 📋 [**`docs/03_base_de_reglas.md`**](docs/03_base_de_reglas.md): Las 30 reglas lógicas de producción agrupadas por módulos operativos (A, B, C, D y E).
* 📊 [**`docs/04_casos_de_uso_y_trazabilidad.md`**](docs/04_casos_de_uso_y_trazabilidad.md): Trazabilidad ciclo a ciclo de los Casos 1, 2 y 3 (equiparación, resolución de conflicto y disparo).
* 💻 [**`docs/05_manual_desarrollador.md`**](docs/05_manual_desarrollador.md): Guía de instalación, ejecución local y despliegue del frontend en Streamlit.
* 🛡️ [**`docs/06_auditoria_bucles_deadlocks.md`**](docs/06_auditoria_bucles_deadlocks.md): Demostración matemática del Grafo Acíclico (DAG, 0 ciclos) y guardas `NOT`.

---

## 📂 Estructura del Repositorio

```text
├── README.md                                  # Portada general y guía rápida
├── GLOSARY.md                                 # Glosario formal y diccionario A-BN
│
├── docs/                                      # Documentación técnica extendida
│   ├── 01_arquitectura_del_sistema.md
│   ├── 02_modelo_de_marcos.md
│   ├── 03_base_de_reglas.md
│   ├── 04_casos_de_uso_y_trazabilidad.md
│   ├── 05_manual_desarrollador.md
│   └── 06_auditoria_bucles_deadlocks.md
│
├── implementacion/                            # Código fuente del motor y notebooks
│   ├── IC2026 - Trabajo de Campo - G2.ipynb   # Cuaderno interactivo unificado para Google Colab
│   ├── main.ipynb                            # Alias estándar del notebook principal
│   ├── Punto2_Arquitecto_Base_Hechos.ipynb    # Cuaderno modular del Punto 2 (Base de Hechos)
│   ├── marcos.py                             # Clases de Marcos y factorías de Memoria de Trabajo
│   ├── reglas_modulos_c_d_e.py               # Reglas R19 a R30 (Módulos C, D y E)
│   └── README.md                             # Guía técnica de la implementación
│
├── frontend/                                  # Aplicación web en Streamlit (Punto 5)
│   ├── app.py                                # Interfaz interactiva y Módulo de Explicación
│   ├── requirements.txt                      # Dependencias del servidor web
│   └── README.md                             # Instrucciones de ejecución
│
├── specs/                                     # Especificaciones técnicas por rol (Protocolo Grill-Me)
│   ├── README.md                             # Protocolo Antialucinación Grill-With-Me
│   ├── 01_coordinador_estudio_evaluativo.md  # Punto 1: Coordinador y Estudio Evaluativo
│   ├── 03_ingeniero_reglas_modulos_a_b.md    # Punto 3: Ingeniero de Reglas 1 (R1 a R18)
│   ├── 04_ingeniero_reglas_modulos_c_d_e.md  # Punto 4: Ingeniero de Reglas 2 (R19 a R30)
│   ├── 05_desarrollador_frontend_explicacion.md # Punto 5: Frontend y Módulo de Explicación
│   └── 06_qa_validador_casos.md              # Punto 6: QA y Validador de Casos
│
└── documentos_referencia/                     # Archivos de educción y fuentes formales
    ├── definicion_de_dominio.txt
    ├── division_de_puntos.txt
    ├── formalizacion_logica.txt
    ├── planificacion_preguntas.txt
    ├── entrevista_inventario.txt
    └── clips_tutorial_ujaen.txt
```

---

## 🚀 Ejecución Rápida

### En Google Colab (1 Clic)
Abre directamente el cuaderno unificado:  
👉 [**Abrir `IC2026 - Trabajo de Campo - G2.ipynb` en Colab**](https://colab.research.google.com/github/Samas1503/proyecto-inco-2026/blob/main/implementacion/IC2026%20-%20Trabajo%20de%20Campo%20-%20G2.ipynb)

### Localmente (Terminal)
```bash
# 1. Clonar el repositorio
git clone https://github.com/Samas1503/proyecto-inco-2026.git
cd proyecto-inco-2026

# 2. Instalar dependencias
pip install -r frontend/requirements.txt

# 3. Iniciar la interfaz interactiva en Streamlit
streamlit run frontend/app.py
```

---

## 📚 Referencias Bibliográficas y Recursos de Estudio

1. **Blancas, Mitchell:** *"Sistema experto y sistema basado en conocimiento - Parte 2 (Programación en Python con Experta)"*. [Video en YouTube](https://youtu.be/wZz7ZKaEyGQ?si=5OfwrloG9d754lfM).
2. **Martínez Santiago, Fernando (Universidad de Jaén):** *"Tutorial de CLIPS (I)"*. [Archivado en Wayback Machine](https://web.archive.org/web/20100510113711/http://wwwdi.ujaen.es/~dofer/ico/material/CLIPS-Tutorial-1.html).
3. **Minsky, Marvin (1974):** *"A Framework for Representing Knowledge"*. MIT-AI Laboratory Memo 306 (Teoría de Marcos / *Frames*).
4. **Cátedra InCo (2026):** Material y guías de Trabajos Prácticos 1 al 5, Facultad de Ingeniería – UNJu.
