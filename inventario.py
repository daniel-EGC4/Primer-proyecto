#! usr/bin/env python3
# Hacer un codigo de una tienda de abarrotes en Python
inventario = {
    "ruffles": {
        "cantidad": 50,
        "precio": 31.50
    },
    "doritos": {
        "cantidad": 30,
        "precio": 32
    },
    "sabritas": {
        "cantidad" : 30,
        "precio": 31
    },
    "runners" : {
        "cantidad" : 30,
        "precio": 35.5
    },
    "leche entera": {
        "cantidad": 25,
        "precio": 27.0
    },
    "huevo blanco": {
        "cantidad": 15,
        "precio": 54.0
    },
    "frijol negro": {
        "cantidad": 40,
        "precio": 38.5
    },
    "arroz": {
        "cantidad": 35,
        "precio": 22.0
    },
    "aceite vegetal": {
        "cantidad": 20,
        "precio": 45.0
    },
    "pan de caja blanco": {
        "cantidad": 18,
        "precio": 48.5
    },
    "refresco cola": {
        "cantidad": 50,
        "precio": 18.0
    },
    "atun en agua": {
        "cantidad": 60,
        "precio": 19.5
    },
    "jabón de tocador": {
        "cantidad": 32,
        "precio": 16.0
    }
}

def mostrar_inventario(nombre):
    return inventario.get(nombre)

def existe_producto(nombre):
    return nombre in inventario

def agregar_producto(nombre, cantidad, precio):
    inventario[nombre] = { "cantidad": cantidad, "precio": precio }

def actualizar_cantidad (nombre, cantidad_nueva):
    if existe_producto(nombre):
        inventario[nombre]["cantidad"] = cantidad_nueva
        return True
    return False

def vender (nombre, cantidad_vendida):
    if not existe_producto(nombre):
        return False
    if inventario[nombre]["cantidad"] < cantidad_vendida:
        return False
    inventario[nombre]["cantidad"] -= cantidad_vendida
    return True