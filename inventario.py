#! usr/bin/env python3
# Hacer un codigo de una tienda de abarrotes en Python

import json
import os

ruta = os.path.dirname (os.path.abspath (__file__))
ruta_json = os.path.join (ruta, "Inventario.Json")
with open (ruta_json, "r", encoding="utf-8") as archivo:
    inventario = json.load (archivo)

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