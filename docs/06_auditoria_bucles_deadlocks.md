# 🛡️ Auditoría Formal: Prevención de Bucles Infinitos y Deadlocks

En los Sistemas Expertos basados en encadenamiento hacia adelante (*forward chaining*), dos de las patologías más graves son:
1. **Bucles Infinitos (*Infinite Loops*):** Reglas que re-aseveran hechos o se disparan cíclicamente sin converger.
2. **Interbloqueos (*Deadlocks*):** Cadenas de producción que quedan truncas porque una regla intermedia no emite el hecho esperado por la siguiente regla.

---

## 1. Verificación Topológica de Dependencias (Grafo Acíclico Dirigido - DAG)

Se modeló la base completa de 30 reglas de producción como un grafo dirigido de transiciones de estado:
* **Vértices ($V$):** Conjunto de las 66 proposiciones ($A \dots BN$).
* **Aristas Dirigidas ($E$):** Dependencias $Premisa \to Conclusion$.

### Algoritmo de Detección de Ciclos
Se ejecutó una búsqueda en profundidad (DFS) con coloreo de tres estados (Blanco: No visitado, Gris: En exploración, Negro: Completado):
* **Resultado del Análisis:** **`0 ciclos detectados`**.
* **Demostración:** Ninguna conclusión generada en los Módulos A, B, C, D o E actúa como premisa de una regla jerárquicamente anterior. Por ejemplo:
  $$Q, R, S \xrightarrow{R_7} T \xrightarrow{R_8} U$$
  Ni $U$ ni $V$ pueden generar $Q$, $R$ o $S$. Por lo tanto, el sistema converge en tiempo finito de forma determinística.

---

## 2. Guardas Anti-Bucle con Patrones de No-Existencia (`NOT`)

### El Problema de las Activaciones Dobles en `OR`
En la librería `experta`, cuando una regla define una disyunción:
```python
@Rule(OR(Marco(...), HechoSimbolico(...)))
```
Si en la Memoria de Trabajo coexisten ambas representaciones (el marco y el símbolo), el algoritmo Rete genera dos activaciones en la Agenda, disparando la regla dos veces consecutivas.

### La Solución Canónica (Guardas `NOT`)
Se implementó en **absolutamente todas las reglas** la verificación de no-existencia del hecho deducido:
```python
@Rule(
    OR(Contexto(temperatura="frio"), HechoSimbolico(codigo="M")),
    NOT(HechoSimbolico(codigo="N")) # Guarda que desactiva la segunda instancia en Rete
)
def regla_05_menu_caliente(self):
    self.declare(HechoSimbolico(codigo="N", desc="Ofrecer menú caliente", valor=True))
```
Al dispararse la primera activación y aseverarse $N$, la red Rete invalida instantáneamente la segunda activación de la agenda, garantizando **un único disparo por regla**.

---

## 3. Resolución de Deadlocks en Transiciones de Estado

### Caso Detectado en la Cadena de Cocina:
* La Regla $R_{22}$ (Fraccionar carne fresca) declaraba la acción $AV$, pero la Regla $R_{23}$ (Congelar) exigía la existencia de la premisa $AW$ ("Carne en folex").
* Si $R_{22}$ solo emitía $AV$, la cadena quedaba en **deadlock** ($R_{23}$ nunca se activaba).
* **Solución:** $R_{22}$ asevera tanto la acción de fraccionamiento ($AV$) como el nuevo estado físico del insumo ($AW$ y `Insumo(estado="fraccionada_en_folex")`), permitiendo el flujo continuo hacia $R_{23}$ y $R_{24}$.

---

## 4. Calibración de Salience contra Condiciones de Carrera

Cuando múltiples reglas compiten en la Agenda, se garantiza la resolución determinística mediante prioridades explícitas:
* **Nivel 20 (Máxima Prioridad):** Regla $R_{28}$ (Inocuidad bromatológica ante carne oscura).
* **Nivel 15 (Prioridad Operativa Alta):** Regla $R_{27}$ (Crisis domingo tarde con carnicerías cerradas).
* **Nivel 10 (Operaciones Estándar):** Reglas de abastecimiento ordinario ($R_{26}$, $R_1$, etc.).
* **Nivel 9 (Encadenamientos Secuenciales):** Reglas dependientes ($R_{23}$, $R_8$, $R_9$).
