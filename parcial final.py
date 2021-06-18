productos = [[10,"paqueteDePapas",2000],
            [20,"gaseosa",1600],
            [30,"empanada",1000],
            [40,"jugoNatural",3000]]

        
bolean2 = True
while bolean2:
    print("1.Comprar producto\n2.Registrar producto")

    opcion =eval(input("Ingrese el numero de la accion que desea realizar: "))
    if opcion == 1:
        cedula = eval(input("Ingrese su numero de cedula o tarjeta de identidad: "))
        rol = int(input("1.Estudiante\n2.Profesor \n Ingrese el numero que corresponda a su rol: "))
        if rol == 1:
            rolImp = "Estudiante"
            desc = 0.50
            producto = eval(input("Ingrese el codigo del producto que desea comprar: "))
            for x in productos:
                if x[0] == producto:
                    bandera = True
                    precio = x[2]
                    precio2 = precio - (precio * desc)
                    print("El " + rolImp + " con cedula " + str(cedula) + ", debe pagar " + str(precio2) + " por el producto " + str(x[0]))
                    break
                else:
                    bandera = False
            if bandera == False:
                print("el codigo del producto no es valido")
            bolean2 = False
        elif rol == 2:
            rolImp = "Profesor"
            desc = 0.20
            producto = eval(input("Ingrese el codigo del producto que desea comprar: "))
            for x in productos:
                if x[0] == producto:
                    bandera = True
                    precio = x[2]
                    precio2 = precio - (precio * desc)
                    print("El " + rolImp + " con cedula " + str(cedula) + ", debe pagar " + str(precio2) + " por el producto " + str(x[0]))
                    break
                else:
                    bandera = False
            if bandera == False:
                print("el codigo del producto no es valido")
            bolean2 = False
        else:
            print("El rol ingresado no existe")

    if opcion == 2:
        nombreProducto = input("Ingrese el nombre del producto que desea agregar: ")
        codigoProducto = eval(input("Ingrese el codigo del producto que desea agregar: "))
        precioN = eval(input("Ingrese el precio del producto que desea agregar: "))
        for y in productos:
            if y[0] == codigoProducto:
                print("Este codigo de producto ya se encuentra registrado")
                break
            else:
                listaN = [codigoProducto,nombreProducto,precioN]
                productos.append(listaN)
                print("La lista de productos ha sido actualizada:\n")
                print(productos)
                break


