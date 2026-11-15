# 📊 Casos de Uso y Trazabilidad del Encadenamiento Hacia Adelante

En este documento se describe la trazabilidad formal de los **3 Casos de Uso** diseñados para verificar la convergencia del algoritmo Rete y el comportamiento del motor de inferencia.

---

## 🍲 Caso 1: Estrategia de Oferta de Menú por Clima Frío y Público Familiar

* **Objetivo:** Deducir la oferta gastronómica y predecir el tipo de plato preferido ante bajas temperaturas y mesas familiares.
* **Memoria de Trabajo Inicial ($BH_0$):** $\{M, W\}$
  * $M$: Temperatura es frío.
  * $W$: Tipo de cliente es Familia.

### Trazabilidad Ciclo por Ciclo

| Ciclo | Equiparación (Reglas Satisfechas) | Conjunto de Conflicto | Resolución de Conflicto | Regla Disparada | Hechos Deducidos | Memoria de Trabajo Resultante |
|:---:|---|:---:|:---:|:---:|:---:|---|
| **0** | — | — | — | — | — | $BH_0 = \{M, W\}$ |
| **1** | $R_5 (M)$: Satisfecha<br>$R_6 (M)$: Satisfecha<br>$R_{10} (W)$: Satisfecha | $\{R_5, R_6, R_{10}\}$ | Regla del Mínimo Subíndice | **$R_5$** | $N$ | $BH_1 = \{M, W, N\}$ |
| **2** | $R_5$: Ya disparada<br>$R_6 (M)$: Satisfecha<br>$R_{10} (W)$: Satisfecha | $\{R_6, R_{10}\}$ | Regla del Mínimo Subíndice | **$R_6$** | $O, P$ | $BH_2 = \{M, W, N, O, P\}$ |
| **3** | $R_5, R_6$: Ya disparadas<br>$R_{10} (W)$: Satisfecha | $\{R_{10}\}$ | Única regla activada | **$R_{10}$** | $X$ | $BH_3 = \{M, W, N, O, P, X\}$ |

* **Conclusión Final:** El restaurante debe sumar sopas y menú caliente ($N$), mantener los sándwiches y pizzas habituales ($O, P$) y anticipar consumo orientado al plato ($X$).

---

## 🍻 Caso 2: Gestión de Demanda por Quincena, Sol y Grupos Grandes

* **Objetivo:** Inferir el comportamiento de consumo atípico y ajustar compras específicas de mercadería.
* **Memoria de Trabajo Inicial ($BH_0$):** $\{Q, R, S\}$
  * $Q$: Fecha es quincena o cobro.
  * $R$: Clima es soleado.
  * $S$: Reservas son grupos grandes.

### Trazabilidad Ciclo por Ciclo

| Ciclo | Equiparación | Conjunto de Conflicto | Resolución | Disparo | Hecho Deducido | Memoria de Trabajo |
|:---:|---|:---:|:---:|:---:|:---:|---|
| **0** | — | — | — | — | — | $BH_0 = \{Q, R, S\}$ |
| **1** | $R_7 (Q, R, S)$: Satisfecha<br>$R_8 (T), R_9 (T)$: Incompletas | $\{R_7\}$ | Única regla activada | **$R_7$** | $T$ | $BH_1 = \{Q, R, S, T\}$ |
| **2** | $R_7$: Ya disparada<br>$R_8 (T)$: Satisfecha ($T \in BH_1$)<br>$R_9 (T)$: Satisfecha ($T \in BH_1$) | $\{R_8, R_9\}$ | Mínimo Subíndice | **$R_8$** | $U$ | $BH_2 = \{Q, R, S, T, U\}$ |
| **3** | $R_7, R_8$: Ya disparadas<br>$R_9 (T)$: Satisfecha ($T \in BH_2$) | $\{R_9\}$ | Única regla activada | **$R_9$** | $V$ | $BH_3 = \{Q, R, S, T, U, V\}$ |

* **Conclusión Final:** Se deduce un comportamiento de alta bebida y baja comida ($T$), decidiendo aumentar compra de destilados y snacks ($U$) y reducir compras de vegetales ($V$) para evitar mermas por vencimiento.

---

## 🚨 Caso 3: Crisis de Abastecimiento un Domingo por la Tarde

* **Objetivo:** Resolver una contingencia operativa crítica ante la falta de carne con proveedores habituales cerrados.
* **Memoria de Trabajo Inicial ($BH_0$):** $\{BC, BF, BG\}$
  * $BC$: Momento es Crítico y Falta Insumo.
  * $BF$: Día es Domingo por la tarde.
  * $BG$: Carnicerías están cerradas.

### Trazabilidad Ciclo por Ciclo

| Ciclo | Equiparación | Conjunto de Conflicto | Resolución | Disparo | Hecho Deducido | Memoria de Trabajo |
|:---:|---|:---:|:---:|:---:|:---:|---|
| **0** | — | — | — | — | — | $BH_0 = \{BC, BF, BG\}$ |
| **1** | $R_{26} (BC, BD)$: Incompleta ($BD \notin BH_0$)<br>$R_{27} (BC, BF, BG)$: Satisfecha | $\{R_{27}\}$ | Única regla activada | **$R_{27}$** | $BH$ | $BH_1 = \{BC, BF, BG, BH\}$ |

* **Conclusión Final:** Al no haber carnicerías abiertas, se descarta mandar un empleado ($R_{26}$) y se ordena la baja inmediata del plato informando a los mozos para ofrecer una alternativa sugerida al comensal ($BH$).
