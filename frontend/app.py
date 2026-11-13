"""
Frontend del Sistema Basado en Conocimiento (SBC) Gastronómico
Trabajo de Campo - Inteligencia del Conocimiento (InCo 2026)
Facultad de Ingeniería - Universidad Nacional de Jujuy (FI-UNJu)

Punto 5: Desarrollador de Interfaz y Módulo de Explicación
Este archivo implementa la estructura en Streamlit para interactuar con la Base de Hechos
(Punto 2) y el Motor de Reglas Lógicas (Puntos 3 y 4).
"""

import sys
import os
import streamlit as st

# Agregar la carpeta de implementación al path para importar los marcos
implementacion_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "implementacion"))
if implementacion_path not in sys.path:
    sys.path.append(implementacion_path)

try:
    from marcos import (
        Contexto, Cliente, Insumo, Proveedor, Operacion,
        HechoSimbolico, DICCIONARIO_PROPOSICIONES,
        cargar_caso_1, cargar_caso_2, cargar_caso_3
    )
    MARCOS_DISPONIBLES = True
except ImportError as e:
    MARCOS_DISPONIBLES = False
    error_import = str(e)

# ---------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA STREAMLIT
# ---------------------------------------------------------
st.set_page_config(
    page_title="SBC Gastronómico - InCo 2026",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Sistema Basado en Conocimiento: Asesor de Inventario Gastronómico")
st.markdown("""
**Cátedra:** Inteligencia del Conocimiento (2026) | **Grupo:** 02 | **FI-UNJu**  
*Optimización inteligente de compras, control de stock y mitigación de desperdicios.*
""")

if not MARCOS_DISPONIBLES:
    st.error(f"⚠️ No se pudo importar `marcos.py` desde `implementacion/`. Detalle: {error_import}")
    st.stop()

# ---------------------------------------------------------
# BARRA LATERAL: SELECCIÓN DE HECHOS INICIALES
# ---------------------------------------------------------
st.sidebar.header("⚙️ Variables de Entrada (Entorno)")

modo_carga = st.sidebar.radio(
    "Modo de Carga de Hechos:",
    ["Carga Rápida (Casos de Prueba)", "Ingreso Manual / Personalizado"]
)

hechos_iniciales = []
explicaciones_paso_a_paso = []

if modo_carga == "Carga Rápida (Casos de Prueba)":
    caso_seleccionado = st.sidebar.selectbox(
        "Seleccionar Escenario Formal:",
        [
            "Caso 1: Ajuste de Menú por Frío y Público Familiar (M, W)",
            "Caso 2: Alta Demanda por Quincena, Sol y Grupos Grandes (Q, R, S)",
            "Caso 3: Crisis por Domingo Tarde y Comercios Cerrados (BC, BF, BG)"
        ]
    )
    
    if "Caso 1" in caso_seleccionado:
        hechos_iniciales = cargar_caso_1()
        st.sidebar.info("💡 **Hechos cargados:** Temperatura fría ($M$) y Cliente Familia ($W$).")
    elif "Caso 2" in caso_seleccionado:
        hechos_iniciales = cargar_caso_2()
        st.sidebar.info("💡 **Hechos cargados:** Quincena ($Q$), Clima soleado ($R$) y Grupos grandes ($S$).")
    elif "Caso 3" in caso_seleccionado:
        hechos_iniciales = cargar_caso_3()
        st.sidebar.info("💡 **Hechos cargados:** Quiebre de stock ($BC$), Domingo tarde ($BF$) y Carnicerías cerradas ($BG$).")

else:
    # Ingreso manual
    dia = st.sidebar.selectbox("Día de la semana:", ["habil", "fin_de_semana", "domingo"])
    momento = st.sidebar.selectbox("Momento del día:", ["manana", "tarde", "noche"])
    temperatura = st.sidebar.selectbox("Temperatura:", ["templado", "frio", "calido"])
    clima = st.sidebar.selectbox("Clima:", ["soleado", "nublado", "lluvioso"])
    tipo_cliente = st.sidebar.selectbox("Perfil del comensal:", ["familia", "jovenes", "general"])
    es_quincena = st.sidebar.checkbox("Es semana de cobro / quincena", value=False)
    faltante_critico = st.sidebar.checkbox("Hay faltante crítico de mercadería", value=False)
    
    # Construcción de hechos
    hechos_iniciales.append(Contexto(
        dia=dia, momento=momento, temperatura=temperatura,
        clima=clima, es_quincena=es_quincena
    ))
    hechos_iniciales.append(Cliente(tipo=tipo_cliente))
    if faltante_critico:
        hechos_iniciales.append(Operacion(quiebre_stock_critico=True))

# ---------------------------------------------------------
# CUERPO PRINCIPAL: VISUALIZACIÓN DE HECHOS Y RESULTADOS
# ---------------------------------------------------------
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Memoria de Trabajo Inicial ($WM_0$)")
    st.write("Hechos declarados en la base de hechos listos para equiparación:")
    for i, h in enumerate(hechos_iniciales, 1):
        st.code(f"Hecho #{i}: {h}", language="python")

with col2:
    st.subheader("🚀 Ejecución del Motor de Inferencia")
    st.write("Disparo secuencial de reglas según encadenamiento hacia adelante:")
    
    boton_ejecutar = st.button("🔥 Ejecutar Encadenamiento Hacia Adelante", type="primary")

    if boton_ejecutar:
        st.success("Motor de Inferencia activado.")
        
        # Simulación / Hook para que los Puntos 3, 4 y 5 conecten el motor final
        st.markdown("### 📢 Decisiones Operativas Deducidas:")
        
        # Identificar qué caso o hechos se activaron
        codigos_presentes = [h.get("codigo") for h in hechos_iniciales if isinstance(h, dict) and "codigo" in h]
        
        if "M" in codigos_presentes or any(h.get("temperatura") == "frio" for h in hechos_iniciales if isinstance(h, dict)):
            st.info("🍲 **Oferta de Menú:** Ofrecer menú caliente y sopas (Regla R5: $M \\implies N$).")
            st.info("🍕 **Menú Habitual:** Mantener sándwiches y pizzas tradicionales (Regla R6: $M \\implies O, P$).")
            explicaciones_paso_a_paso.append("R5 y R6 se dispararon por detección de temperatura fría ($M$).")
            
        if "W" in codigos_presentes or any(h.get("tipo") == "familia" for h in hechos_iniciales if isinstance(h, dict)):
            st.info("🍽️ **Comportamiento:** Comensales orientados a menú al plato (Regla R10: $W \\implies X$).")
            explicaciones_paso_a_paso.append("R10 se disparó por perfil de cliente 'Familia' ($W$).")

        if "Q" in codigos_presentes and "R" in codigos_presentes and "S" in codigos_presentes:
            st.warning("🍻 **Demanda Prevista:** Alta rotación de bebidas y bajo consumo de comida (Regla R7: $Q, R, S \\implies T$).")
            st.warning("🥃 **Abastecimiento:** Aumentar compra de destilados y snacks (Regla R8: $T \\implies U$).")
            st.warning("🥦 **Ajuste de Compras:** Reducir compras de vegetales para evitar mermas (Regla R9: $T \\implies V$).")
            explicaciones_paso_a_paso.append("R7 dedujo comportamiento T; luego R8 y R9 ajustaron compras específicas.")

        if "BC" in codigos_presentes and "BF" in codigos_presentes and "BG" in codigos_presentes:
            st.error("🚨 **Protocolo de Crisis:** Dar de baja inmediata del plato sin stock y ofrecer sustituto sugerido (Regla R27: $BC, BF, BG \\implies BH$).")
            explicaciones_paso_a_paso.append("R27 se disparó por quiebre de stock un domingo por la tarde sin comercios abiertos.")

# ---------------------------------------------------------
# MÓDULO DE EXPLICACIÓN (TRANSPARENCIA COGNITIVA)
# ---------------------------------------------------------
st.divider()
st.subheader("💡 Módulo de Explicación (Trazabilidad y Justificación)")

if explicaciones_paso_a_paso:
    for exp in explicaciones_paso_a_paso:
        st.markdown(f"- ✅ **Justificación:** {exp}")
else:
    st.caption("Presiona el botón de ejecución para ver la justificación paso a paso de cada regla disparada.")
