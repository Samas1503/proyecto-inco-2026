# Especificación Técnica: Punto 6 – Analista de Pruebas (QA) y Validador de Casos

## 👤 Rol
* **Rol:** Analista de Calidad (QA) y Validador de Casos de Uso
* **Entregable Principal:** Suite de pruebas automatizadas o notebook de validación que certifique formalmente la ejecución de los **3 Casos de Uso** de la Actividad 4, garantizando la convergencia del algoritmo Rete, la ausencia de ciclos infinitos y la trazabilidad exacta de la Agenda de reglas.

---

## 📚 Documentación y Referencias de Implementación

1. **Guía Teórica de CLIPS (Universidad de Jaén):** [`documentos_referencia/clips_tutorial_ujaen.txt`](../documentos_referencia/clips_tutorial_ujaen.txt).
   * Monitoreo de activaciones con `(agenda)`, trazabilidad de inserciones (`==>`), eliminaciones (`<==`) y disparos (`FIRE`).
   * Resolución del Conjunto de Conflicto mediante la **Regla del Mínimo Subíndice** o salience.
2. **Clase Magistral de Mitchell Blancas:** [Sistema experto y SBC con Experta en Python](https://youtu.be/wZz7ZKaEyGQ).
   * Verificación del encadenamiento hacia adelante conducido por datos y captura de aserciones.
3. **Formalización Lógica de los 3 Casos:** [`documentos_referencia/formalizacion_logica.txt`](../documentos_referencia/formalizacion_logica.txt).

---

## 🎯 Casos de Prueba a Certificar (Tablas de Trazabilidad Actividad 4)

### Caso 1: Estrategia de Oferta de Menú y Demanda por Clima Frío y Familia
* **Hechos Iniciales ($BH_0$):** $\{M, W\}$
* **Ciclo 1:**
  * *Equiparación:* Reglas $R_5 (M)$, $R_6 (M)$, $R_{10} (W)$ satisfechas.
  * *Conjunto de Conflicto:* $\{R_5, R_6, R_{10}\}$.
  * *Resolución de Conflicto:* Se selecciona $R_5$ (Regla del Mínimo Subíndice / Salience).
  * *Disparo:* Se infiere $N$ $\implies BH_1 = \{M, W, N\}$.
* **Ciclo 2:**
  * *Equiparación:* $R_6 (M)$, $R_{10} (W)$ satisfechas.
  * *Conjunto de Conflicto:* $\{R_6, R_{10}\}$.
  * *Resolución de Conflicto:* Se selecciona $R_6$.
  * *Disparo:* Se infiere $O, P$ $\implies BH_2 = \{M, W, N, O, P\}$.
* **Ciclo 3:**
  * *Equiparación:* $R_{10} (W)$ satisfecha.
  * *Conjunto de Conflicto:* $\{R_{10}\}$.
  * *Disparo:* Se infiere $X$ $\implies BH_3 = \{M, W, N, O, P, X\}$.
* **Aserción de Test:** Validar que la Memoria de Trabajo final contenga exactamente $N, O, P, X$.

---

### Caso 2: Gestión de Demanda por Quincena, Clima Soleado y Grupos Grandes
* **Hechos Iniciales ($BH_0$):** $\{Q, R, S\}$
* **Ciclo 1:**
  * *Equiparación:* $R_7 (Q, R, S)$ satisfecha.
  * *Disparo:* Se deduce el comportamiento $T$ $\implies BH_1 = \{Q, R, S, T\}$.
* **Ciclo 2:**
  * *Equiparación:* $R_8 (T)$ y $R_9 (T)$ satisfechas.
  * *Resolución de Conflicto:* Se selecciona $R_8$.
  * *Disparo:* Se deduce $U$ (aumentar destilados) $\implies BH_2 = \{Q, R, S, T, U\}$.
* **Ciclo 3:**
  * *Equiparación:* $R_9 (T)$ satisfecha.
  * *Disparo:* Se deduce $V$ (reducir vegetales) $\implies BH_3 = \{Q, R, S, T, U, V\}$.
* **Aserción de Test:** Validar que se hayan inferido $T$, $U$ y $V$ en ese orden estricto.

---

### Caso 3: Protocolo de Crisis un Domingo por la Tarde con Carnicerías Cerradas
* **Hechos Iniciales ($BH_0$):** $\{BC, BF, BG\}$
* **Ciclo 1:**
  * *Equiparación:* 
    * $R_{26} (BC, BD)$ queda incompleta porque comercios cercanos $BD \notin BH_0$.
    * $R_{27} (BC, BF, BG)$ queda satisfecha.
  * *Conjunto de Conflicto:* $\{R_{27}\}$.
  * *Disparo:* Se deduce $BH$ (Dar de baja plato y ofrecer alternativa) $\implies BH_1 = \{BC, BF, BG, BH\}$.
* **Aserción de Test:** Validar que $R_{26}$ no se dispare y que $BH$ sea el único hecho de crisis aseverado.

---

## 🛠️ Requisitos Técnicos de las Pruebas
1. **Calibración de Salience:**
   * Ajustar los valores de `salience` numéricos en el motor para que el algoritmo Rete dispare en el orden exacto de subíndices de la Actividad 4 ($R_5 \to R_6 \to R_{10}$ y $R_8 \to R_9$).
2. **Prevención de Ciclos Infinitos:**
   * Garantizar que las pruebas terminen en tiempo finito sin que ninguna regla re-dispare sobre hechos preexistentes.
3. **Formato de Salida de Pruebas:**
   * Cada prueba debe imprimir en consola las secuencias de activación emulando `(watch facts)` y `(watch rules)` de CLIPS:
     ```text
     ==> Inserción de Hecho Inicial: Contexto(temperatura='frio')
     [FIRE R5] -> Deducido: HechoSimbolico(codigo='N')
     [OK] Caso 1 Validado: Hechos deducidos {N, O, P, X} coinciden con la formalización.
     ```

---

## 🛑 Protocolo Mandatorio `Grill-With-Me` para este Punto

Antes de escribir el código de las pruebas con una IA, **el asistente debe interrogarte** sobre:
1. *¿Qué mecanismo usaremos para probar el motor: un script `test_casos.py` con `assert`, o un notebook interactivo de validación con celdas de prueba?*
2. *¿Cómo verificaremos que el orden de resolución del conjunto de conflicto respete los ciclos teóricos documentados?*
3. *¿Qué casos de prueba negativos o con datos contradictorios diseñaremos para demostrar la resiliencia del SBC ante los profesores?*
