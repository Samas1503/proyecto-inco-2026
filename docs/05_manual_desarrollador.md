# 💻 Manual del Desarrollador e Integrador

Guía técnica paso a paso para configurar el entorno, ejecutar los cuadernos en Google Colab, correr el frontend en Streamlit y validar los casos de prueba.

---

## 🛠️ Requisitos Previos e Instalación

### Opción 1: Ejecución en Google Colab (Recomendada)
1. Abre [Google Colab](https://colab.research.google.com).
2. Abre o sube el cuaderno principal [`implementacion/IC2026 - Trabajo de Campo - G2.ipynb`](../implementacion/IC2026%20-%20Trabajo%20de%20Campo%20-%20G2.ipynb).
3. Ejecuta la celda de inicio que aplica automáticamente el parche para Python 3.10+:
   ```python
   !pip install frozendict experta --quiet
   ```
4. Ejecuta las celdas en orden secuencial.

---

### Opción 2: Ejecución Local en Linux / macOS / Windows
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Samas1503/proyecto-inco-2026.git
   cd proyecto-inco-2026
   ```
2. Crea y activa un entorno virtual (recomendado Python 3.9 o 3.10):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```
3. Instala dependencias:
   ```bash
   pip install -r frontend/requirements.txt
   ```
4. Para ejecutar las pruebas de los marcos y el motor:
   ```bash
   python3 implementacion/marcos.py
   python3 implementacion/reglas_modulos_c_d_e.py
   ```

---

## 🖥️ Ejecución del Frontend en Streamlit

Para iniciar la interfaz gráfica interactiva:

```bash
streamlit run frontend/app.py
```

El navegador abrirá la aplicación en `http://localhost:8501`.
* **Carga de Casos:** Utiliza la barra lateral para alternar entre los Casos 1, 2 y 3.
* **Módulo de Explicación:** Al presionar *"Ejecutar Encadenamiento Hacia Adelante"*, el panel inferior mostrará la justificación de cada regla activada.
