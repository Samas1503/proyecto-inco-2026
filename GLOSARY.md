# 📖 Glosario Técnico del Sistema Basado en Conocimiento (GLOSARY)
### Optimización de Inventarios y Mitigación de Desperdicios en Gastronomía
**Cátedra:** Inteligencia del Conocimiento (InCo 2026) – Facultad de Ingeniería, UNJu  
**Grupo 02**

---

## 📑 Índice de Contenidos
1. [Conceptos de Ingeniería del Conocimiento y Sistemas de Producción](#1-conceptos-de-ingeniería-del-conocimiento-y-sistemas-de-producción)
2. [Conceptos del Dominio Gastronómico e Inventarios](#2-conceptos-del-dominio-gastronómico-e-inventarios)
3. [Diccionario Canónico de las 66 Proposiciones (A – BN)](#3-diccionario-canónico-de-las-66-proposiciones-a--bn)
4. [Estructura de Marcos de Marvin Minsky (Frames)](#4-estructura-de-marcos-de-marvin-minsky-frames)

---

## 1. Conceptos de Ingeniería del Conocimiento y Sistemas de Producción

* **Algoritmo Rete:** Algoritmo eficiente de emparejamiento de patrones diseñado por Charles Forgy en 1974. Construye una red acíclica de nodos para evaluar hechos contra reglas sin necesidad de reevaluar todas las combinaciones en cada ciclo. Es el núcleo motor de CLIPS y de la librería Experta.
* **Agenda:** Cola estructurada donde se almacenan las instancias de reglas que han sido activadas (cuyas precondiciones se han cumplido) y están listas para dispararse.
* **Aserción (`assert` / `declare`):** Operación fundamental mediante la cual se introduce un nuevo hecho a la Memoria de Trabajo del sistema experto.
* **Base de Conocimiento (BC):** Componente permanente del Sistema Basado en Conocimiento que almacena las reglas formales de inferencia (conocimiento heurístico y procedimental del experto).
* **Base de Hechos (BH / Working Memory - MT):** Memoria de trabajo dinámica donde residen los hechos conocidos actualmente sobre el entorno o problema (estado del mundo). Varía ciclo a ciclo durante la inferencia ($BH_0 \to BH_1 \dots \to BH_n$).
* **Conjunto de Conflicto:** Subconjunto de la Agenda que contiene todas las reglas cuyas premisas han sido satisfechas simultáneamente en un ciclo de inferencia determinado.
* **Encadenamiento Hacia Adelante (*Forward Chaining*):** Estrategia de inferencia dirigida por datos (*data-driven*). Comienza con los hechos conocidos en la Memoria de Trabajo y aplica reglas de producción para derivar nuevos hechos o acciones hasta alcanzar un estado final o meta.
* **Encadenamiento Hacia Atrás (*Backward Chaining*):** Estrategia de inferencia dirigida por metas (*goal-driven*). Comienza con una hipótesis o meta y busca recursivamente en la base de reglas qué hechos deben cumplirse para validarla (paradigma nativo de Prolog).
* **Equiparación (*Pattern Matching*):** Fase del ciclo de inferencia donde el motor evalúa las precondiciones de las reglas contra el estado actual de la Memoria de Trabajo.
* **Faceta Procedimental (*Daemon*):** Procedimiento o función asociada a una ranura de un marco que se activa automáticamente cuando se accede a dicha ranura, se altera su valor o se detecta una anomalía (ej. detección de carne oscura).
* **Guarda Anti-Bucle (`NOT`):** Condición de no-existencia colocada en la precondición de una regla para evitar que se re-dispare indefinidamente una vez que su conclusión ya fue aseverada.
* **Hecho Atómico / Proposicional:** Representación simplificada del conocimiento basada en una única variable o código unívoco booleano (ej. $M$: Temperatura es frío).
* **LHS (*Left-Hand Side*):** Precondición o antecedente de una regla de producción ("SI...").
* **Marco (*Frame*):** Estructura propuesta por Marvin Minsky (1974) para representar conceptos o situaciones estereotipadas mediante una colección estructurada de atributos llamados ranuras (*slots*) y valores asociados.
* **Módulo de Explicación (*Explainability*):** Subsistema de un Sistema Experto responsable de justificar ante el usuario final el razonamiento seguido, explicando qué hechos motivaron cada deducción y qué reglas se ejecutaron.
* **Ranura (*Slot*):** Atributo específico o propiedad elemental que describe un aspecto particular dentro de un Marco (ej. en `MarcoContexto`, la ranura `temperatura`).
* **Resolución de Conflictos:** Estrategia heurística empleada por el motor de inferencia para decidir qué regla disparar cuando varias reglas compiten en el Conjunto de Conflicto. Estrategias comunes incluyen: Regla del Mínimo Subíndice, Mayor Especificidad, Novedad (*Recency*) o Prioridad Explícita (*Salience*).
* **Retracción (`retract`):** Operación de borrado que elimina un hecho obsoleto o consumido de la Memoria de Trabajo.
* **RHS (*Right-Hand Side*):** Consecuente o postcondición de una regla de producción ("ENTONCES...").
* **Salience (Prioridad Numérica):** Atributo entero asignado a una regla que determina su prelación en la Agenda. Reglas con mayor salience numérico se disparan antes que reglas con menor salience.

---

## 2. Conceptos del Dominio Gastronómico e Inventarios

* **Comanda:** Pedido formal emitido desde el salón o la barra hacia la cocina, especificando los platos o bebidas solicitados por una mesa.
* **Desperdicio / Merma Bromatológica:** Insumo perecedero que pierde sus propiedades de inocuidad o calidad organoléptica (ej. carne que cambia a color oscuro) y debe retirarse de la venta al público.
* **Estiba FIFO / PEPS:** Principio de almacenamiento "Primero en Entrar, Primero en Salir" (*First In, First Out*). Exige acomodar la mercadería recién llegada en la parte trasera del depósito o estantería, dejando los insumos más antiguos al frente para su consumo prioritario.
* **Folex:** Lámina plástica separadora utilizada para fraccionar cortes de carne fresca en porciones unitarias antes de su congelación rápida, evitando que se adhieran entre sí.
* **Quiebre de Stock (*Stockout*):** Situación crítica donde el inventario disponible de un ingrediente o insumo esencial se agota durante el servicio, impidiendo despachar los platos de la carta.
* **Rotación de Insumos:** Velocidad con la que se consume y repone un producto en el local:
  * *Muy rápida:* Insumos de consumo masivo diario (cerveza, hielo).
  * *Rápida:* Insumos de producción base diaria (pre-pizzas, queso, jamón, salsa).
  * *Normal / Baja:* Insumos secos o no perecederos en depósito.

---

## 3. Diccionario Canónico de las 66 Proposiciones (A – BN)

A continuación se detalla la semántica formal de cada una de las 66 proposiciones diseñadas en la Actividad 4 y codificadas en `implementacion/marcos.py`:

| Código | Significado / Descripción Formal | Categoría | Ranura Asociada | Valor Formal |
|:---:|---|:---:|---|:---:|
| **A** | Día es Fin de semana | Contexto | `dia` | `"fin_de_semana"` |
| **B** | Día es Domingo | Contexto | `dia` | `"domingo"` |
| **C** | Aumentar compra de mercadería | Acción / Decisión | `compra` | `"aumentar"` |
| **D** | Surtir para mañana, tarde y noche | Acción / Decisión | `turnos_abastecimiento` | `"todos"` |
| **E** | Evento es Partido Boca/River | Contexto | `evento` | `"boca_river"` |
| **F** | Planificar turnos temprano y tarde | Acción / Decisión | `turnos_personal` | `"temprano_y_tarde"` |
| **G** | Comprar bebidas de forma gradual | Acción / Decisión | `estrategia_bebida` | `"gradual"` |
| **H** | No comprar bebidas de golpe | Acción / Decisión | `estrategia_bebida` | `"no_de_golpe"` |
| **I** | Evento es Desfile 23 de Agosto | Contexto | `evento` | `"desfile_23_agosto"` |
| **J** | Competencia es Alta | Contexto | `competencia` | `"alta"` |
| **K** | Reducir expectativa de demanda | Acción / Decisión | `expectativa_demanda` | `"reducida"` |
| **L** | Evitar sobrestock | Acción / Decisión | `riesgo_stock` | `"evitar_sobrestock"` |
| **M** | Temperatura es frío | Contexto | `temperatura` | `"frio"` |
| **N** | Ofrecer menú caliente (sopas) | Acción / Decisión | `oferta_menu` | `"caliente_sopas"` |
| **O** | Mantener menú habitual | Acción / Decisión | `oferta_menu` | `"mantener_habitual"` |
| **P** | Ofrecer sándwiches y pizzas | Acción / Decisión | `oferta_menu` | `"sandwiches_pizzas"` |
| **Q** | Fecha es quincena o cobro | Contexto | `es_quincena` | `True` |
| **R** | Clima es soleado | Contexto | `clima` | `"soleado"` |
| **S** | Reservas son grupos grandes | Cliente | `reservas` | `"grupos_grandes"` |
| **T** | Comportamiento es Alta Bebida y Baja Comida | Cliente | `comportamiento` | `"alta_bebida_baja_comida"` |
| **U** | Aumentar compra de destilados y snacks | Acción / Decisión | `compras_especificas` | `"mas_destilados_snacks"` |
| **V** | Reducir compra de vegetales | Acción / Decisión | `compras_especificas` | `"menos_vegetales"` |
| **W** | Tipo de cliente es Familia | Cliente | `tipo` | `"familia"` |
| **X** | Preferencia es Menú al plato | Cliente | `preferencia` | `"menu_al_plato"` |
| **Y** | Tipo de cliente es Jóvenes | Cliente | `tipo` | `"jovenes"` |
| **Z** | Preferencia es Bebidas y sándwiches | Cliente | `preferencia` | `"bebidas_y_sandwiches"` |
| **AA** | Producto es Cerveza | Insumo | `nombre` | `"cerveza"` |
| **AB** | Prioridad de compra es Alta y Rotación muy rápida | Acción / Decisión | `prioridad_rotacion` | `"alta_muy_rapida"` |
| **AC** | Producto es Pre-pizza, Queso, Jamón o Salsa | Insumo | `categoria` | `"pizza_y_aderezos"` |
| **AD** | Prioridad de compra es Alta y Rotación rápida | Acción / Decisión | `prioridad_rotacion` | `"alta_rapida"` |
| **AE** | Tarea es Compra Diaria | Operación | `tarea` | `"compra_diaria"` |
| **AF** | Desplazarse a mercados favoritos | Acción / Decisión | `metodo_compra` | `"mercados_favoritos"` |
| **AG** | Pagar con Efectivo, Transferencia o Tarjeta | Acción / Decisión | `medios_pago` | `"efectivo_transferencia_tarjeta"` |
| **AH** | Dueña no está disponible | Operación | `duena_disponible` | `False` |
| **AI** | Delegar compra a Encargada de caja | Acción / Decisión | `delegacion` | `"encargada_caja"` |
| **AJ** | Producto es Hielo | Insumo | `nombre` | `"hielo"` |
| **AK** | Origen de compra son Proveedores Fijos | Acción / Decisión | `origen_compra` | `"proveedores_fijos"` |
| **AL** | Local favorito no sostiene precio | Proveedor | `sostiene_precio` | `False` |
| **AM** | Otro local tiene precio más barato | Proveedor | `precio_mas_barato` | `True` |
| **AN** | Cambiar de local/proveedor | Acción / Decisión | `decision_proveedor` | `"cambiar_proveedor"` |
| **AO** | Producto es Bebida Blanca, Gaseosa o Vino | Insumo | `categoria` | `"bebidas_generales"` |
| **AP** | Destino de almacenamiento es Depósito | Acción / Decisión | `almacenamiento` | `"deposito"` |
| **AQ** | Ingresa mercadería nueva | Operación | `tarea` | `"ingreso_mercaderia"` |
| **AR** | Ubicar nuevo atrás y viejo adelante (PEPS) | Acción / Decisión | `criterio_estiba` | `"peps_fifo"` |
| **AS** | Producto es Carne o Comida Diaria | Insumo | `categoria` | `"perecedero_diario"` |
| **AT** | Tiempo de guardado corto y compra diaria | Acción / Decisión | `politica_stock` | `"guardado_corto_diario"` |
| **AU** | Producto es Carne fresca | Insumo | `nombre` | `"carne"` |
| **AV** | Separar en porciones con folex | Acción / Decisión | `manipulacion` | `"fraccionar_con_folex"` |
| **AW** | Producto es Carne fraccionada en folex | Insumo | `estado` | `"fraccionada_en_folex"` |
| **AX** | Congelar porciones | Acción / Decisión | `conservacion` | `"congelar"` |
| **AY** | Ingresa comanda de Carne | Operación | `comanda` | `"carne"` |
| **AZ** | Sacar porción congelada directo a plancha | Acción / Decisión | `coccion` | `"directo_a_plancha"` |
| **BA** | Llega mercadería al local | Operación | `tarea` | `"llegada_mercaderia"` |
| **BB** | Acomodar lugares y conservar para horas pico | Acción / Decisión | `operacion_salon` | `"preparar_para_pico"` |
| **BC** | Momento es Crítico y Falta Insumo | Operación | `quiebre_stock_critico` | `True` |
| **BD** | Negocios cercanos abiertos | Proveedor | `cercanos_abiertos` | `True` |
| **BE** | Mandar empleado a comprar de urgencia | Acción / Decisión | `gestion_crisis` | `"comprar_urgencia_empleado"` |
| **BF** | Día es Domingo por la tarde | Contexto | `horario_critico` | `"domingo_tarde"` |
| **BG** | Carnicerías están cerradas | Proveedor | `carnicerias_abiertas` | `False` |
| **BH** | Dar de baja producto y ofrecer alternativa | Acción / Decisión | `gestion_crisis` | `"baja_producto_y_alternativa"` |
| **BI** | Color de carne es oscuro | Insumo | `apariencia_carne` | `"color_oscuro"` |
| **BJ** | Separar de venta y cocinar para animales | Acción / Decisión | `destino_merma` | `"separar_y_cocinar_animales"` |
| **BK** | Aumenta costo de carne | Insumo | `aumento_costo_carne` | `True` |
| **BL** | Aumenta precio de plato | Acción / Decisión | `ajuste_precio` | `"trasladar_al_plato"` |
| **BM** | Aumenta costo de bebida | Insumo | `aumento_costo_bebida` | `True` |
| **BN** | Mantener precio de bebida | Acción / Decisión | `ajuste_precio` | `"mantener_precio_bebida"` |

---

## 4. Estructura de Marcos de Marvin Minsky (Frames)

El conocimiento heurístico del sistema se estructura en 5 clases de marcos semánticos basadas en la clase base `Fact`:

### 1. `MarcoContexto` (Alias: `Contexto`)
Encapsula el entorno meteorológico, de calendario y de demanda externa:
* `dia`: `'lunes'`, `'martes'`, ..., `'domingo'`, `'fin_de_semana'`.
* `momento`: `'manana'`, `'tarde'`, `'noche'`.
* `horario_critico`: `'domingo_tarde'`, `'ninguno'`.
* `temperatura`: `'frio'`, `'templado'`, `'calido'`.
* `clima`: `'soleado'`, `'nublado'`, `'lluvioso'`.
* `es_quincena`: Booleano (`True` si coincide con fecha de cobro).
* `evento`: `'boca_river'`, `'desfile_23_agosto'`, `'ninguno'`.
* `competencia`: `'alta'`, `'normal'`, `'baja'`.

### 2. `MarcoCliente` (Alias: `Cliente`)
Encapsula el perfil de los comensales y el patrón de consumo inferido:
* `tipo`: `'familia'`, `'jovenes'`, `'ejecutivo'`, `'general'`.
* `reservas`: `'grupos_grandes'`, `'mesas_chicas'`, `'ninguna'`.
* `comportamiento`: `'alta_bebida_baja_comida'`, `'estandar'`.
* `preferencia`: `'menu_al_plato'`, `'bebidas_y_sandwiches'`.

### 3. `MarcoInsumo` (Alias: `Insumo`)
Encapsula el estado bromatológico, la conservación y la rotación de los productos:
* `nombre`: Nombre del ingrediente (`'carne'`, `'cerveza'`, `'hielo'`, `'queso'`, etc.).
* `categoria`: `'perecedero_diario'`, `'bebidas_generales'`, `'pizza_y_aderezos'`.
* `estado`: `'fresco'`, `'fraccionada_en_folex'`, `'congelada'`, `'en_deposito'`.
* `apariencia_carne`: `'normal'`, `'color_oscuro'`.
* `aumento_costo_carne`: Booleano.
* `aumento_costo_bebida`: Booleano.
* `rotacion`: `'muy_rapida'`, `'rapida'`, `'normal'`.
* `stock_critico`: Booleano.

### 4. `MarcoProveedor` (Alias: `Proveedor`)
Encapsula la disponibilidad de abastecimiento externo y comercios:
* `tipo`: `'fijo'`, `'mercado_favorito'`, `'cercano'`, `'carniceria'`.
* `carnicerias_abiertas`: Booleano.
* `cercanos_abiertos`: Booleano.
* `sostiene_precio`: Booleano.
* `precio_mas_barato`: Booleano.

### 5. `MarcoOperacion` (Alias: `Operacion`)
Encapsula el flujo operativo de salón y las contingencias:
* `tarea`: `'compra_diaria'`, `'ingreso_mercaderia'`, `'llegada_mercaderia'`.
* `comanda`: Insumo demandado por cocina (`'carne'`, `'sandwiches'`, etc.).
* `duena_disponible`: Booleano (`False` dispara delegación de compras).
* `quiebre_stock_critico`: Booleano (`True` activa protocolos de crisis).

### 6. `HechoSimbolico`
Puente híbrido para emparejar directamente las letras formales del diccionario:
* `codigo`: String unívoco de proposición (ej. `'M'`, `'W'`, `'BC'`).
* `desc`: Descripción formal legible.
* `valor`: Booleano o valor escalar.
