import inventario as inv

precio_final = 0
lista_productos = []

def busqueda (precio_final, lista_productos):
    start = input("Desea empezar a comprar? (si/no): ")
    while start.lower() == "si":
        nombre = input("Ingrese el nombre del producto: ").lower()
        cantidad = int(input("Ingrese la cantidad: "))
        
        if inv.existe_producto(nombre):
            info_producto = inv.mostrar_inventario(nombre)
            precio_unitario = info_producto["precio"]
            precio_total = precio_unitario * cantidad
            precio_final += precio_total
            lista_productos.append((nombre))
            print(f"Producto agregado: {nombre}")
        else:
            print("El producto no existe en el inventario.")
        
        start = input("Desea agregar otro producto? (si/no): ")
    print (f"La lista de compras es: {lista_productos}\n")
    print (f"El precio final es: {precio_final:.2f}")
    
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

busqueda(precio_final, lista_productos)