# Especificación Técnica: Punto 3 – Ingeniero de Reglas Lógicas 1 (Módulos A y B)

## 👤 Rol
* **Rol:** Ingeniero de Reglas Lógicas 1
* **Entregable:** Módulo de reglas en Python (`reglas_modulos_a_b.py`) o celdas correspondientes en el Colab principal, programando las **Reglas 1 a 18** con la librería `experta`.

---

## 🎯 Alcance de Reglas a Implementar

Debes traducir estrictamente al decorador `@Rule` de `experta` las reglas formalizadas en `documentos_referencia/formalizacion_logica.txt`:

### Módulo A: Predicción de Demanda y Oferta de Menú
* **Regla 1:** $A \lor B \implies C, D$ (Fin de semana o Domingo $\implies$ Aumentar compra mercadería y surtir m/t/n).
* **Regla 2:** $E \implies F$ (Partido Boca/River $\implies$ Planificar turnos temprano y tarde).
* **Regla 3:** $E \implies G, H$ (Partido Boca/River $\implies$ Comprar bebidas gradual y no de golpe).
* **Regla 4:** $I \land J \implies K, L$ (Desfile 23 de Agosto y Competencia alta $\implies$ Reducir demanda y evitar sobrestock).
* **Regla 5:** $M \implies N$ (Temperatura fría $\implies$ Ofrecer menú caliente y sopas).
* **Regla 6:** $M \implies O, P$ (Temperatura fría $\implies$ Mantener menú habitual y ofrecer sándwiches/pizzas).
* **Regla 7:** $Q \land R \land S \implies T$ (Quincena, Clima soleado y Grupos grandes $\implies$ Alta Bebida y Baja Comida).
* **Regla 8:** $T \implies U$ (Comportamiento T $\implies$ Aumentar destilados y snacks).
* **Regla 9:** $T \implies V$ (Comportamiento T $\implies$ Reducir compra de vegetales).
* **Regla 10:** $W \implies X$ (Cliente Familia $\implies$ Preferencia Menú al plato).
* **Regla 11:** $Y \implies Z$ (Cliente Jóvenes $\implies$ Preferencia Bebidas y sándwiches).

### Módulo B: Adquisición, Prioridades y Proveedores
* **Regla 12:** $AA \implies AB$ (Producto Cerveza $\implies$ Prioridad alta y rotación muy rápida).
* **Regla 13:** $AC \implies AD$ (Producto Pre-pizza/Queso/Jamón/Salsa $\implies$ Prioridad alta y rotación rápida).
* **Regla 14:** $AE \implies AF$ (Compra diaria $\implies$ Desplazarse a mercados favoritos).
* **Regla 15:** $AE \implies AG$ (Compra diaria $\implies$ Pagar con efectivo/transferencia/tarjeta).
* **Regla 16:** $AH \implies AI$ (Dueña no disponible $\implies$ Delegar compra a encargada de caja).
* **Regla 17:** $AJ \lor AA \implies AK$ (Hielo o Cerveza $\implies$ Proveedores fijos).
* **Regla 18:** $AL \land AM \implies AN$ (Local favorito no sostiene precio y otro más barato $\implies$ Cambiar proveedor).

---

## 🛠️ Reglas de Programación Obligatorias
1. **Importación canónica:** Importar los marcos desde `marcos.py`:
   ```python
   from marcos import (
       Rule, KnowledgeEngine, Contexto, Cliente, Insumo,
       Proveedor, Operacion, HechoSimbolico, OR, AND
   )
   ```
2. **Compatibilidad Híbrida:** Cada regla debe poder equipararse con el Marco Semántico y con el `HechoSimbolico` usando `OR`:
   ```python
   @Rule(
       OR(
           Contexto(temperatura="frio"),
           HechoSimbolico(codigo="M")
       )
   )
   def regla_5_clima_frio(self):
       # Declarar hecho N
       self.declare(HechoSimbolico(codigo="N", desc="Ofrecer menú caliente (sopas)", valor=True))
   ```

---

## 🛑 Protocolo Mandatorio `Grill-With-Me` para este Punto

Antes de programar las reglas, **la IA debe interrogarte** sobre:
1. *¿Cómo manejaremos la salience (prioridades numéricas) en reglas concurrentes como R5 y R6?*
2. *¿Las acciones inferidas deben declararse como nuevos `Fact` simbólicos o mutar el marco original en la memoria de trabajo?*
3. *¿Qué mensaje exacto de trazabilidad imprimirá cada regla al dispararse en consola para el Punto 5?*
