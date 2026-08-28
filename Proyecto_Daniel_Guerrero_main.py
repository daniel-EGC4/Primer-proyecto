import inventario as inv

precio_final = 0
lista_productos = []

start = input("Desea empezar a comprar? (si/no): ")
while start.lower() == "si":
    nombre = input("Ingrese el nombre del producto: ")
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