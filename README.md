# RecuperatorioParcial1
Recuperatorio del primer parcial para programacion 1 - UTN TUPAD - Grille Agustina


## 📋 ¿Qué hace este programa?

Al ejecutarse, muestra un menú de opciones con 5 acciones posibles. El programa permanece activo hasta que el usuario elige finalizarlo.

### Opciones disponibles:

1. **Mostrar listado de stock disponible**
   - Imprime en pantalla todos los productos actuales con sus respectivas cantidades.

2. **Consultar stock de un producto específico**
   - Permite ingresar el nombre de un producto para consultar cuántas unidades hay en stock.
   - Si el producto no existe, informa al usuario.

3. **Ver productos sin stock**
   - Recorre el listado y muestra solo aquellos productos cuya cantidad es igual a 0.
   - Si todos tienen stock, lo indica.

4. **Agregar productos**
   - Permite ingresar el nombre y la cantidad de un nuevo producto.
   - Valida que la cantidad ingresada sea un número entero.
   - Da la opción de seguir agregando productos o volver al menú principal.
   - No se evita el ingreso de nombres repetidos.

5. **Finalizar programa**
   - Cierra la ejecución del programa.

---

## 🔍 Validaciones implementadas

- Menú principal: solo acepta números del 1 al 5.
- Al ingresar cantidad de un producto, se valida que sea un número entero positivo con `.isdigit()`.
- Solo se aceptan respuestas `"Y"` o `"N"` (en mayúsculas) al preguntar si se desea seguir agregando productos.

---

## 📌 Notas importantes

- El programa **no utiliza `try/catch`** por decisión pedagógica, pero se comenta en el código que sería una buena práctica en producción.
- No se evita la repetición de productos en el stock (puede haber productos con el mismo nombre).
- Las listas se inicializan con una carga mínima de datos (`"cacao"`, `"arroz"`, `"pollo"`, `"mani"`).

---

## 🧑‍💻 Autor/a: Agustina Ariadna Grille

Trabajo práctico desarrollado como parte de la resolucion del recuperatorio del primer parcial de Programacion I - UTN
