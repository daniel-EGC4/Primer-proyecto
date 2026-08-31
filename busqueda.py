#! usr/bin/env python3
import inventario as inv

precio_final = 0
lista_productos = []

def buscar (nombre, cantidad, lista_productos, precio_acumulado):
    """
    Recibe el estado actual de la compra y un producto nuevo a agregar.
    No usa input() ni print() - solo procesa y regresa resultados.
    """

    nombre = nombre.lower().strip()
    
    if not nombre:
        return lista_productos, precio_acumulado, "Ingrese un nombre de producto"
    
    if not inv.existe_producto(nombre):
        return lista_productos, precio_acumulado, f"'{nombre}' no existe en el inventario"
    
    info_producto = inv.mostrar_inventario(nombre)
    precio_total = info_producto["precio"] * cantidad
    nuevo_precio_acumulado = precio_acumulado + precio_total
    lista_productos.append(nombre)
    
    mensaje = f"Agregado: {nombre} x{cantidad} (${precio_total:.2f})"
    return lista_productos, nuevo_precio_acumulado, mensaje


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
    else:
        print ("Pudrase pues")
