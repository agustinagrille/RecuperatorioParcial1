#Inicializo las variables de listados, desisto de crearlas vacias para que en la ejecucion ya tengan una data minima cargada.
listadoNombreProductos = ["cacao", "arroz", "pollo", "mani"] 
listadoCantidadDeProductos = [5, 3, 10, 0]

#Inicio de ciclo while para seleccion de opciones
while True:
    print(f"1- Mostrar listado de stock disponible")
    print(f"2- Consultar stock de un producto especifico")
    print(f"3- Ver productos sin stock")
    print(f"4- Agregar productos")
    print(f"5- Finalizar programa")

    opcionElegida = input("Selecciona una de las 5 opciones para avanzar: ")
    #Inicio validacion de opcion elegida
    if opcionElegida in ["1", "2", "3", "4"]:
        if opcionElegida == "1":
            print("Listado de productos completo:")
            for i in range (len(listadoNombreProductos)):
                print(f"{listadoNombreProductos[i]} cantidad de stock: {listadoCantidadDeProductos[i]} total")
        elif opcionElegida == "2":
            productoElegido = input("Completa el nombre del producto a consultar: ")
            if productoElegido in listadoNombreProductos:
                indexConsulta = listadoNombreProductos.index(productoElegido)
                print(f"El producto {listadoNombreProductos[indexConsulta]} tiene en stock {listadoCantidadDeProductos[indexConsulta]} unidades.")
            else:
                print("Este producto no se encuentra en el stock actual.")
        elif opcionElegida == "3":
            noHayAgotados = True
            for i in range(len(listadoNombreProductos)):
                if listadoCantidadDeProductos[i] == 0:
                    print(f"Producto: {listadoNombreProductos[i]} sin stock.")
                    noHayAgotados = False
            if noHayAgotados:
                print("No hay productos agotados en stock.")
        else:
            print("Agrega productos al stock")
            """
            A partir de esta instancia de la ejecución lo ideal seria agregar un try/catch para que se pueda evitar 
            cualquier tipo de error de valor al moemnto de la creacion del nuevo producto
            Como aun no vimos ese tema, desisto de tomarlo, y en su lugar, utilizo un metodo while como validador del input, 
            pero es una mala practica no utilizarlos.               
            """
            nombreNuevoProducto = input("Ingresa el nombre del producto: ")
            while True:
                cantidadInput = input("Ingresa la cantidad EN NÚMERO ENTERO de productos: ") #ingreso cantidad para validar si realmente es un entero
                while not cantidadInput.isdigit(): #Valido si efectivamente es un entero, y si no, solicito que se ingrese nuevamente y hasta que sea un entero.
                    print("ERROR: Solo se permiten números enteros. Por favor, proba nuevamente.")
                    cantidadInput = input("Ingresa la cantidad EN NÚMERO ENTERO de productos: ")
                cantidadNuevoProducto = int(cantidadInput)  # Ahora sí es seguro convertirlo
                listadoNombreProductos.append(nombreNuevoProducto)
                listadoCantidadDeProductos.append(cantidadNuevoProducto)
                validoWhile = input(f"Desea agregar un nuevo producto? Y/N ")
                if validoWhile == "Y" or validoWhile == "N":
                    if validoWhile == "N":
                        break
                else:
                    print("Por favor seleccione unicamente Y o N en MAYUSCULAS")

    elif opcionElegida == "5":
        break #Cierro ciclo completo
    else:
        print("ERROR: Por favor coloque un numero entre 1 y 5.") #Validador de errores para el menu principal