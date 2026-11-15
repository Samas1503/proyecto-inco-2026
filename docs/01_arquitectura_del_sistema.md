# 🏛️ Arquitectura del Sistema Basado en Conocimiento

El **Sistema Basado en Conocimiento (SBC)** desarrollado para la cátedra de Inteligencia del Conocimiento (InCo 2026) tiene como finalidad emular el razonamiento heurístico del experto gastronómico en la toma de decisiones diarias sobre compra, conservación y mitigación de desperdicios de mercadería.

---

## 🧩 Componentes Principales del SBC

El sistema sigue la arquitectura clásica de un **Sistema de Producción** moderno con integración orientada a objetos:

```text
  ┌─────────────────────────────────────────────────────────────┐
  │                    INTERFAZ DE USUARIO                      │
  │     (Frontend en Streamlit / Notebook Google Colab)         │
  └──────────────────────────────┬──────────────────────────────┘
                                 │ Hechos de entrada / Consultas
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │               MOTOR DE INFERENCIA (EXPERTA)                 │
  │                                                             │
  │   ┌────────────────────┐          ┌─────────────────────┐   │
  │   │ MEMORIA DE TRABAJO │          │ AGENDA (CONFLICTO)  │   │
  │   │  (Base de Hechos)  │◄────────►│ Resolución Salience │   │
  │   │  Marcos y Símbolos │          │   Mínimo Subíndice  │   │
  │   └─────────┬──────────┘          └──────────┬──────────┘   │
  │             │                                │              │
  │             ▼                                ▼              │
  │   ┌─────────────────────────────────────────────────────┐   │
  │   │             RED RETE DE EQUIPARACIÓN                │   │
  │   └─────────────────────────▲───────────────────────────┘   │
  │                             │                               │
  │   ┌─────────────────────────┴───────────────────────────┐   │
  │   │             BASE DE CONOCIMIENTO (REGLAS)           │   │
  │   │   Módulos A, B (Punto 3) y Módulos C, D, E (Punto 4)│   │
  │   └─────────────────────────────────────────────────────┘   │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │                   MÓDULO DE EXPLICACIÓN                     │
  │     (Traza paso a paso de reglas disparadas y motivos)      │
  └─────────────────────────────────────────────────────────────┘
```

---

## ⚙️ Principios Arquitectónicos Clave

### 1. Paradigma de Inferencia Dirigido por Datos (*Data-Driven*)
El restaurante no opera buscando validar una hipótesis fija (*backward chaining*), sino que reacciona continuamente ante el flujo de eventos del entorno (temperatura del día, tipo de cliente presente, quiebre de stock un domingo por la tarde). Por tanto, la arquitectura utiliza **Encadenamiento Hacia Adelante (*Forward Chaining*)** nativo impulsado por la red Rete.

### 2. Representación Híbrida del Conocimiento
Para superar la rigidez de las proposiciones atómicas sin perder compatibilidad con el diseño teórico de la Actividad 4:
* **Marcos Semánticos (Teoría de Minsky):** Agrupan atributos contextuales en entidades coherentes (`MarcoContexto`, `MarcoCliente`, `MarcoInsumo`, `MarcoProveedor`, `MarcoOperacion`).
* **Hechos Simbólicos (`HechoSimbolico`):** Replican directamente los códigos atómicos ($A \dots BN$), permitiendo que las reglas puedan dispararse tanto por atributos ricos como por código proposicional.

### 3. Modularidad y Desacoplamiento
El motor está compuesto por mixins independientes:
* **Base de Hechos y Marcos:** Desarrollado en [`implementacion/marcos.py`](../implementacion/marcos.py) (Punto 2).
* **Módulos A y B (Predicción y Compras):** Responsabilidad del Punto 3.
* **Módulos C, D y E (Conservación, Crisis y Mermas):** Desarrollado en [`implementacion/reglas_modulos_c_d_e.py`](../implementacion/reglas_modulos_c_d_e.py) (Punto 4).
* **Frontend Web:** Desarrollado en [`frontend/app.py`](../frontend/app.py) (Punto 5).
