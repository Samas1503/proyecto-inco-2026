# 🧱 Modelo de Marcos de Conocimiento (*Frames*)

El modelado del conocimiento se fundamenta en la **Teoría de Marcos de Marvin Minsky (1974)**. Un marco representa una estructura de datos cognitiva para organizar un conjunto estereotipado de conocimientos sobre objetos, roles o situaciones del dominio gastronómico.

---

## 🏗️ Implementación de Marcos en Python (`experta.Fact`)

Cada marco del dominio se define como una clase que hereda de `Fact`, compuesta por ranuras (*slots*) que almacenan valores descriptivos y facetas procedimentales:

### 1. `MarcoContexto`
Representa las variables ambientales, temporales y externas que condicionan la demanda del comensal.
* **Ranuras (*Slots*):**
  * `dia`: `'lunes'`, `'martes'`, ..., `'domingo'`, `'fin_de_semana'` (Mapea $A, B$).
  * `momento`: `'manana'`, `'tarde'`, `'noche'`.
  * `horario_critico`: `'domingo_tarde'`, `'ninguno'` (Mapea $BF$).
  * `temperatura`: `'frio'`, `'templado'`, `'calido'` (Mapea $M$).
  * `clima`: `'soleado'`, `'nublado'`, `'lluvioso'` (Mapea $R$).
  * `es_quincena`: Booleano (Mapea $Q$).
  * `evento`: `'boca_river'`, `'desfile_23_agosto'`, `'ninguno'` (Mapea $E, I$).
  * `competencia`: `'alta'`, `'normal'`, `'baja'` (Mapea $J$).

### 2. `MarcoCliente`
Representa la segmentación de la clientela y las inferencias sobre sus patrones de gasto y preferencias.
* **Ranuras (*Slots*):**
  * `tipo`: `'familia'`, `'jovenes'`, `'ejecutivo'`, `'general'` (Mapea $W, Y$).
  * `reservas`: `'grupos_grandes'`, `'mesas_chicas'`, `'ninguna'` (Mapea $S$).
  * `comportamiento`: `'alta_bebida_baja_comida'`, `'estandar'` (Mapea $T$).
  * `preferencia`: `'menu_al_plato'`, `'bebidas_y_sandwiches'` (Mapea $X, Z$).

### 3. `MarcoInsumo`
Representa las características físicas, rotación y condiciones bromatológicas de los ingredientes.
* **Ranuras (*Slots*):**
  * `nombre`: `'carne'`, `'cerveza'`, `'hielo'`, etc. (Mapea $AA, AJ, AU$).
  * `categoria`: `'perecedero_diario'`, `'bebidas_generales'`, `'pizza_y_aderezos'` (Mapea $AC, AO, AS$).
  * `estado`: `'fresco'`, `'fraccionada_en_folex'`, `'congelada'`, `'en_deposito'` (Mapea $AW$).
  * `apariencia_carne`: `'normal'`, `'color_oscuro'` (Mapea $BI$).
  * `aumento_costo_carne`: Booleano (Mapea $BK$).
  * `aumento_costo_bebida`: Booleano (Mapea $BM$).
  * `rotacion`: `'muy_rapida'`, `'rapida'`, `'normal'` (Mapea $AB, AD$).
  * `stock_critico`: Booleano.

### 4. `MarcoProveedor`
Representa el estado operativo de los proveedores y mercados de abastecimiento.
* **Ranuras (*Slots*):**
  * `tipo`: `'fijo'`, `'mercado_favorito'`, `'cercano'`, `'carniceria'` (Mapea $AK$).
  * `carnicerias_abiertas`: Booleano (Mapea $BG$).
  * `cercanos_abiertos`: Booleano (Mapea $BD$).
  * `sostiene_precio`: Booleano (Mapea $AL$).
  * `precio_mas_barato`: Booleano (Mapea $AM$).

### 5. `MarcoOperacion`
Representa el estado dinámico del servicio en cocina y salón.
* **Ranuras (*Slots*):**
  * `tarea`: `'compra_diaria'`, `'ingreso_mercaderia'`, `'llegada_mercaderia'` (Mapea $AE, AQ, BA$).
  * `comanda`: `'carne'`, `'sandwiches'`, etc. (Mapea $AY$).
  * `duena_disponible`: Booleano (Mapea $AH$).
  * `quiebre_stock_critico`: Booleano (Mapea $BC$).

---

## ⚡ Facetas Procedimentales (*Daemons*)

En este SBC, las facetas procedimentales están modeladas como reglas reactivas de alta prioridad (`salience` elevado) que se disparan en el momento exacto en que un marco cambia de estado:
* **Faceta Bromatológica (Regla 28):** Si la ranura `apariencia_carne` del marco `Insumo` toma el valor `'color_oscuro'`, se activa inmediatamente la acción de retirar el lote de la venta comercial y cocinarlo para animales callejeros.
* **Faceta de Ajuste de Carta (Reglas 29 y 30):** Si se detecta un aumento en el costo de los insumos, el sistema aplica la política comercial automáticamente (trasladar a precio de plato en carnes, mantener precio en bebidas).
