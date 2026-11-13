# Especificación Técnica: Punto 6 – Analista de Pruebas (QA) y Validador de Casos

## 👤 Rol
* **Rol:** Analista de Pruebas (QA) y Validador de Casos
* **Entregable:** Suite de pruebas automatizadas o notebook de validación que ejecute los 3 Casos de Uso formales y demuestre la ausencia de bucles infinitos, la correcta resolución de conflictos y el respeto a las prioridades lógicas.

---

## 🎯 Objetivos Específicos
1. **Validación Formal de los 3 Casos de Uso (Actividad 4):**
   * **Caso 1 (Ajuste por Clima y Público):**
     * $BH_0 = \{M, W\}$
     * Ciclo 1: Disparo de $R_5 \implies N$.
     * Ciclo 2: Disparo de $R_6 \implies O, P$.
     * Ciclo 3: Disparo de $R_{10} \implies X$.
     * $BH_3 = \{M, W, N, O, P, X\}$.
   * **Caso 2 (Alta Demanda por Quincena y Reservas):**
     * $BH_0 = \{Q, R, S\}$
     * Ciclo 1: Disparo de $R_7 \implies T$.
     * Ciclo 2: Disparo de $R_8 \implies U$.
     * Ciclo 3: Disparo de $R_9 \implies V$.
     * $BH_3 = \{Q, R, S, T, U, V\}$.
   * **Caso 3 (Crisis de Abastecimiento un Domingo por la Tarde):**
     * $BH_0 = \{BC, BF, BG\}$
     * Ciclo 1: Disparo de $R_{27} \implies BH$ ($R_{26}$ descartada por premisa incompleta $BD$).
     * $BH_1 = \{BC, BF, BG, BH\}$.
2. **Control de Ciclos Infinitos y Resolución de Conflictos:**
   * Verificar que ninguna regla re-dispare indefinidamente sobre el mismo hecho.
   * Ajustar la **salience** (prioridades numéricas en `@Rule(salience=...)`) para garantizar que se respete la estrategia de resolución de conflictos de la cátedra (ej. Regla del Mínimo Subíndice o Especificidad).
3. **Reporte de Cobertura y Trazabilidad:**
   * Comprobar que las salidas por consola y en los asserts coincidan exactamente carácter por carácter con las tablas de equiparación de la Actividad 4.

---

## 🛑 Protocolo Mandatorio `Grill-With-Me` para este Punto

Antes de escribir el código de pruebas, **la IA debe interrogarte** sobre:
1. *¿Qué framework de testing se utilizará? (¿`pytest`, `unittest` nativo de Python, o aserciones directas en celdas de Colab?)*
2. *¿Cómo validaremos que los hechos intermedios se infirieron en el orden exacto de los ciclos teóricos?*
3. *¿Qué casos límite o escenarios de fallo forzado (edge cases) presentaremos a los profesores para demostrar la robustez del motor?*
