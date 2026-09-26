import inventario as inv
def menu():
    respuesta_menu = input("Quiere ver el menú? (si/no): ")
    start = "no"
    if respuesta_menu.lower() == "si":
        print(f"{'ID':<5}| {'Producto':<35}| {'Precio':>10} | {'Cantidad':>9}")
        print("-" * 75)
        for ID, datos in inventario.items():
            print(f"{ID:<5}| {datos['nombre']:<35}| {datos['precio']:>8}\t| {datos['cantidad']:>5}")
        start = "si"
    elif respuesta_menu.lower() == "no":
        start = input("Desea empezar a comprar? (si/no): ")
    else:
        print("Por favor, rellene correctamente el campo")
    return start

def busqueda(start):
    precio_final = 0
    lista_productos = []
    #Sistema de menú
    while start.lower() == "si":
        ID = input("Ingrese el ID del producto: ")
        if ID.lower() == "0":
            break
        else:
            try:
                cantidad = int(input("Ingrese la cantidad: "))
            except ValueError:
                print("Ingrese una cantidad numérica válida.")
                start = input("Desea agregar otro producto? (si/no): ")
                continue

        #Busquedas de productos
        if inv.existe_producto(ID):
            #se extrae el producto y todos los datos de el
            info_producto = inv.mostrar_inventario(ID)
            if not inv.vender (ID, cantidad):
                print ("no hay cantidad suficiente")
                continue
            #se extrae el precio unitario de cada producto
            precio_unitario = info_producto["precio"]
            #se consigue el precio total multiplicando el precio de cada producto por la cantidad que se va a comprar
            precio_total = precio_unitario * cantidad
            #Se suma el precio final por el precio total de los productos introducidos
            precio_final += precio_total

            lista_productos.append(info_producto["nombre"])
            print(f"Producto agregado: {info_producto["nombre"]}")
        else:   
            print("El producto no existe en el inventario.")


    print(f"La lista de compras es: {lista_productos}\n")
    print(f"El precio final es: {precio_final:.2f}")
    return precio_final

def pago(precio_final):
    while precio_final > 0:
        try:
            cobro = float(input("ingrese el dinero del pago: "))
        except ValueError:
            print("Ingrese un valor correcto.")
            continue
        if cobro > precio_final:
            cambio = cobro - precio_final
            print(f"Su cambio es: $ {cambio:.2f}")
            print("Gracias por venir")
            break
        elif cobro < precio_final:
            precio_final -= cobro
            print(f"El cobro es insuficiente, le falta: {precio_final:.2f}")
            continue
        else:
            print("Gracias por venir")
            break

total = busqueda(menu())
pago(total)