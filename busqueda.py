import inventario as inv


lista_productos = []

def busqueda (lista_productos):
    precio_final = 0

    #Sistema de menú
    while True:
        menu = input("Quiere ver el menú? (si/no): ")

        if menu.lower() == "si":
            
            print (f"Producto\t", end="\t")
            print ("Precio\t", end = "\t")
            print ("cantidad")
            for i in range (50):
                print ("-", end="")
            print ()
            for producto, datos in inv.inventario.items ():
                print(f"{producto:<20}| {datos['precio']:>8}\t| {datos['cantidad']:>10}")
            break
        elif menu.lower() == "no":
            break
        else:
            print ("Por favor, rellene correctamente el campo")

    #Sistema de compras
    if menu == "si":
        start = "si"
    else:
        start = input("Desea empezar a comprar? (si/no): ")
    while start.lower() == "si":
        nombre = input("Ingrese el nombre del producto: ").lower()
        cantidad = int(input("Ingrese la cantidad: "))

        #Busquedas de productos
        if inv.existe_producto(nombre):
            #se extrae el producto y todos los datos de el
            info_producto = inv.mostrar_inventario(nombre)
            #se extrae el precio unitario de cada producto
            precio_unitario = info_producto["precio"]
            #se consigue el precio total multiplicando el precio de cada producto por la cantidad que se va a comprar
            precio_total = precio_unitario * cantidad
            #Se suma el precio final por el precio final de los productos introducidos, informaicón extraida en la linea anterior
            precio_final += precio_total
            lista_productos.append((nombre))
            print(f"Producto agregado: {nombre}")
        else:
            print("El producto no existe en el inventario.")
        
        start = input("Desea agregar otro producto? (si/no): ")
        if start.lower() == "no":
            break
    print (f"La lista de compras es: {lista_productos}\n")
    print (f"El precio final es: {precio_final:.2f}")
    return precio_final

def pago (precio_final):
    while precio_final > 0:
        cobro = float(input("ingrese el dinero del pago: "))
        if cobro > precio_final:
            cambio = cobro - precio_final
            print (f"Su cambio es: $ {cambio}")
            print ("Gracias por venir")
            break
        elif cobro < precio_final:
            precio_final -= cobro
            print(f"El cobro es insuficiente, le falta: {precio_final:.2f}")
            continue
        else:
            print ("Gracias por venir")
            break

total = busqueda(lista_productos)
pago (total)