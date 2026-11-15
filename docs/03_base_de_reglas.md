# 📋 Base de Reglas Lógicas de Producción

La Base de Conocimiento del SBC está compuesta por **30 reglas de producción formales**, divididas en 5 módulos operativos:

---

## 🟢 Módulo A: Predicción de Demanda y Oferta de Menú
* **$R_1$:** Si Día es Fin de semana ($A$) o Día es Domingo ($B$) $\implies$ Aumentar compra de mercadería ($C$) y Surtir para mañana, tarde y noche ($D$).
* **$R_2$:** Si Evento es Partido Boca/River ($E$) $\implies$ Planificar turnos temprano y tarde ($F$).
* **$R_3$:** Si Evento es Partido Boca/River ($E$) $\implies$ Comprar bebidas de forma gradual ($G$) y No de golpe ($H$).
* **$R_4$:** Si Evento es Desfile 23 de Agosto ($I$) y Competencia es Alta ($J$) $\implies$ Reducir expectativa de demanda ($K$) y Evitar sobrestock ($L$).
* **$R_5$:** Si Temperatura es frío ($M$) $\implies$ Ofrecer menú caliente y sopas ($N$).
* **$R_6$:** Si Temperatura es frío ($M$) $\implies$ Mantener menú habitual ($O$) y Ofrecer sándwiches y pizzas ($P$).
* **$R_7$:** Si Fecha es quincena ($Q$), Clima es soleado ($R$) y Reservas son grupos grandes ($S$) $\implies$ Comportamiento es Alta Bebida y Baja Comida ($T$).
* **$R_8$:** Si Comportamiento es Alta Bebida y Baja Comida ($T$) $\implies$ Aumentar compra de destilados y snacks ($U$).
* **$R_9$:** Si Comportamiento es Alta Bebida y Baja Comida ($T$) $\implies$ Reducir compra de vegetales ($V$).
* **$R_{10}$:** Si Tipo de cliente es Familia ($W$) $\implies$ Preferencia es Menú al plato ($X$).
* **$R_{11}$:** Si Tipo de cliente es Jóvenes ($Y$) $\implies$ Preferencia es Bebidas y sándwiches ($Z$).

---

## 🟡 Módulo B: Adquisición, Prioridades y Proveedores
* **$R_{12}$:** Si Producto es Cerveza ($AA$) $\implies$ Prioridad de compra es Alta y Rotación muy rápida ($AB$).
* **$R_{13}$:** Si Producto es Pre-pizza, Queso, Jamón o Salsa ($AC$) $\implies$ Prioridad de compra es Alta y Rotación rápida ($AD$).
* **$R_{14}$:** Si Tarea es Compra Diaria ($AE$) $\implies$ Desplazarse a mercados favoritos ($AF$).
* **$R_{15}$:** Si Tarea es Compra Diaria ($AE$) $\implies$ Pagar con Efectivo, Transferencia o Tarjeta ($AG$).
* **$R_{16}$:** Si Dueña no está disponible ($AH$) $\implies$ Delegar compra a Encargada de caja ($AI$).
* **$R_{17}$:** Si Producto es Hielo ($AJ$) o Cerveza ($AA$) $\implies$ Origen de compra son Proveedores Fijos ($AK$).
* **$R_{18}$:** Si Local favorito no sostiene precio ($AL$) y Otro local tiene precio más barato ($AM$) $\implies$ Cambiar de local/proveedor ($AN$).

---

## 🔵 Módulo C: Almacenamiento y Conservación
* **$R_{19}$:** Si Producto es Bebida Blanca, Gaseosa o Vino ($AO$) $\implies$ Destino de almacenamiento es Depósito ($AP$).
* **$R_{20}$:** Si Ingresa mercadería nueva ($AQ$) $\implies$ Ubicar nuevo atrás y viejo adelante según PEPS/FIFO ($AR$).
* **$R_{21}$:** Si Producto es Carne o Comida Diaria ($AS$) $\implies$ Tiempo de guardado corto y compra diaria ($AT$).
* **$R_{22}$:** Si Producto es Carne fresca ($AU$) $\implies$ Separar en porciones con folex ($AV$) y Habilitar estado carne en folex ($AW$).
* **$R_{23}$:** Si Producto es Carne en folex ($AW$) $\implies$ Congelar inmediatamente ($AX$).
* **$R_{24}$:** Si Ingresa comanda de Carne ($AY$) $\implies$ Sacar porción congelada directo a plancha ($AZ$).
* **$R_{25}$:** Si Llega mercadería al local ($BA$) $\implies$ Acomodar lugares y conservar para horas pico ($BB$).

---

## 🔴 Módulo D: Operación en Servicio y Control de Crisis
* **$R_{26}$:** Si Momento es Crítico y Falta Insumo ($BC$) y Negocios cercanos abiertos ($BD$) $\implies$ Mandar empleado a comprar de urgencia ($BE$).
* **$R_{27}$:** Si Momento es Crítico y Falta Insumo ($BC$), Día es Domingo tarde ($BF$) y Carnicerías cerradas ($BG$) $\implies$ Dar de baja producto y ofrecer alternativa gastronómica ($BH$).

---

## 🟣 Módulo E: Control de Mermas y Ajuste de Precios
* **$R_{28}$:** Si Color de carne es oscuro ($BI$) $\implies$ Separar de venta y cocinar para animales de la calle ($BJ$).
* **$R_{29}$:** Si Aumenta costo de carne ($BK$) $\implies$ Aumenta precio de venta del plato ($BL$).
* **$R_{30}$:** Si Aumenta costo de bebida ($BM$) $\implies$ Mantener precio de venta de bebida para fidelizar ($BN$).
