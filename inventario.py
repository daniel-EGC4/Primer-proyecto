#! usr/bin/env python3
# Hacer un codigo de una tienda de abarrotes en Python
import json
import os

ruta = os.path.dirname (os.path.abspath (__file__))
ruta_json = os.path.join (ruta, "Inventario.Json")
with open (ruta_json, "r", encoding="utf-8") as archivo:
    inventario = json.load (archivo)


def mostrar_inventario(ID):
    return inventario.get(ID)

def existe_producto(ID):
    return ID in inventario

def agregar_producto(ID, nombre,cantidad, precio):
    inventario[ID] = { "nombre" : nombre, "cantidad": cantidad, "precio": precio }

def actualizar_cantidad (ID, cantidad_nueva):
    if existe_producto(ID):
        inventario[ID]["cantidad"] = cantidad_nueva
        return True
    return False

def vender (ID, cantidad_vendida):
    if not existe_producto(ID):
        return False
    if inventario[ID]["cantidad"] < cantidad_vendida:
        return False
    inventario[ID]["cantidad"] -= cantidad_vendida
    return True
