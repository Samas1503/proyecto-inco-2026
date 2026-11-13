# 🖥️ Frontend en Streamlit – SBC Gastronómico (InCo 2026)

Interfaz web interactiva desarrollada para el **Punto 5: Desarrollador de Interfaz y Módulo de Explicación**, conectada a la Base de Hechos del **Punto 2** y preparada para integrar las reglas de los **Puntos 3 y 4**.

---

## 🚀 Cómo ejecutar la aplicación

1. **Instalar dependencias necesarias:**
   ```bash
   pip install -r frontend/requirements.txt
   ```

2. **Iniciar el servidor Streamlit:**
   ```bash
   streamlit run frontend/app.py
   ```

3. Se abrirá automáticamente en tu navegador en `http://localhost:8501`.

---

## 🎯 Características
* **Selector de Escenarios Formales:** Carga en 1 clic los Casos 1, 2 y 3 formalizados en la Actividad 4.
* **Modo de Ingreso Manual:** Permite al usuario/docente seleccionar día, clima, comensales y faltantes.
* **Visualización de Memoria de Trabajo ($WM_0$):** Muestra los hechos declarados antes de inferir.
* **Módulo de Explicación:** Justifica qué regla se disparó y por qué motivo se tomó cada decisión operativa.
