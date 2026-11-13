# Implementación del Trabajo de Campo – Inteligencia del Conocimiento (InCo)
## Punto 2: Arquitecto de Base de Hechos (Modelado de Marcos / Frames)

Este directorio contiene la solución completa y ejecutable correspondiente al **Punto 2** de la división de tareas del Trabajo de Campo:

* **Responsable:** Arquitecto de Base de Hechos
* **Objetivo:** Traducir el diccionario formal de 66 proposiciones ($A$ a $BN$) y el diseño del inventario del experto gastronómico a código ejecutable en Python utilizando la librería `experta` bajo la teoría de Marcos (*Frames*) de Marvin Minsky.

---

## 📂 Contenido del Directorio

1. **[`IC2026 - Trabajo de Campo - G2.ipynb`](file:///home/samas1503/Descargas/materias/inco/Trabajo%20de%20Campo/implementacion/IC2026%20-%20Trabajo%20de%20Campo%20-%20G2.ipynb)** (y su alias **[`main.ipynb`](file:///home/samas1503/Descargas/materias/inco/Trabajo%20de%20Campo/implementacion/main.ipynb)**):
   * Cuaderno principal del proyecto (reemplaza a `Untitled0.ipynb` siguiendo el estándar del grupo `IC2026 - TP0X - G2`).
2. **[`Punto2_Arquitecto_Base_Hechos.ipynb`](file:///home/samas1503/Descargas/materias/inco/Trabajo%20de%20Campo/implementacion/Punto2_Arquitecto_Base_Hechos.ipynb)**:
   * Notebook enfocado específicamente en la entrega individual/modular del Punto 2.
3. **[`marcos.py`](file:///home/samas1503/Descargas/materias/inco/Trabajo%20de%20Campo/implementacion/marcos.py)**:
   * Módulo independiente de Python listo para ser importado por los **Puntos 3 y 4 (Ingenieros de Reglas Lógicas 1 y 2)** y el **Punto 5 (Desarrollador de Interfaz)**.

---

## 🏗️ Arquitectura de Marcos de Conocimiento (*Frames*)

Se implementó un diseño **híbrido semántico-proposicional**:

| Clase de Marco | Concepto del Dominio | Ranuras Principales (*Slots*) | Proposiciones Asociadas |
|---|---|---|---|
| `MarcoContexto` / `Contexto` | Entorno y Calendario | `dia`, `temperatura`, `clima`, `es_quincena`, `evento`, `competencia`, `horario_critico` | $A, B, E, I, J, M, Q, R, BF$ |
| `MarcoCliente` / `Cliente` | Demanda y Comensales | `tipo`, `reservas`, `comportamiento`, `preferencia` | $S, T, W, X, Y, Z$ |
| `MarcoInsumo` / `Insumo` | Productos e Inventario | `nombre`, `categoria`, `estado`, `rotacion`, `aumento_costo_carne`, `aumento_costo_bebida`, `stock_critico` | $AA, AC, AJ, AO, AS, AU, AW, BI, BK, BM$ |
| `MarcoProveedor` / `Proveedor` | Abastecimiento y Mercados | `tipo`, `carnicerias_abiertas`, `cercanos_abiertos`, `sostiene_precio`, `precio_mas_barato` | $AK, AL, AM, BD, BG$ |
| `MarcoOperacion` / `Operacion` | Operatoria y Crisis | `tarea`, `comanda`, `duena_disponible`, `quiebre_stock_critico` | $AE, AH, AQ, AY, BA, BC$ |
| `HechoSimbolico` | Proposicional Directo | `codigo`, `desc`, `valor` | Las 66 proposiciones ($A \dots BN$) |

---

## 🚀 Cómo consumir este módulo en los siguientes puntos

### Para los Ingenieros de Reglas (Puntos 3 y 4):
En sus respectivos módulos de reglas, pueden importar directamente las clases y los hechos:

```python
from marcos import Rule, Contexto, Cliente, Insumo, Proveedor, Operacion, HechoSimbolico, OR, AND

# Regla usando atributos del marco semántico:
@Rule(Contexto(temperatura="frio"))
def regla_menu_caliente(self):
    print("Sugerencia: Ofrecer sopas por baja temperatura.")

# O regla usando equiparación proposicional directa (código formal):
@Rule(HechoSimbolico(codigo="M"))
def regla_menu_caliente_simbolica(self):
    print("Sugerencia: Ofrecer sopas (Proposición M).")
```

### Para el Validador de Casos y Pruebas (Punto 6):
Pueden cargar inmediatamente los escenarios formales de prueba de la Actividad 4:

```python
from marcos import cargar_caso_1, cargar_caso_2, cargar_caso_3

# Inyectar el Caso 1 en el motor:
hechos = cargar_caso_1()
for h in hechos:
    motor.declare(h)
motor.run()
```

---

## ⚙️ Compatibilidad y Ejecución Local / Google Colab

1. **En Google Colab:**
   * La primera celda del notebook ejecuta automáticamente:
     ```python
     !pip install frozendict experta --quiet
     ```
   * Aplica un parche dinámico para que `collections.Mapping` (requerido internamente por `experta`) funcione sin incompatibilidades en Python 3.10+.
2. **En Entorno Local (sin Experta instalada):**
   * El archivo `marcos.py` cuenta con un fallback de seguridad en Python puro que permite importar las clases y correr los tests estructurales sin lanzar excepciones.
