"""Realizar un programa en Python que calcule el total a pagar en entradas al estadio el CAMPIN.
El estadio cuenta con los siguientes sectores codificados y sus respectivos precios:
Sectores del estadio
A- Norte alta $15.000
B- Norte baja $13.000
C- Oriental alta $10.000
D- Occidental alta $11.000
E- Exclusivo $20.000

El programa debe imprimir:
• Precio Unitario de la boleta
• Cantidad de entradas compradas
• Total a pagar Nota: Validar que la cantidad de boletas debe ser un entero positivo.
"""

nombre_sector = {
    "A": {"nombre": "Norte alta", "precio": 15000},
    "B": {"nombre": "Norte baja", "precio": 13000},
    "C": {"nombre": "Oriental alta", "precio": 10000},
    "D": {"nombre": "Occidental alta", "precio": 11000},
    "E": {"nombre": "Exclusivo", "precio": 20000},
}

# Lista con las claves correspondientes a las opciones
sectores = ["A", "B", "C", "D", "E"]

cesta_de_compra = {}
opcion = 1  # Seleccionamos la opción 1
sector = sectores[opcion - 1]  # Usamos el índice para acceder a la clave correcta
cantidad_boletas = 3  # Cantidad de boletas

cesta_de_compra[nombre_sector[sector]["nombre"]] = {
    "precio": nombre_sector[sector]["precio"],
    "cantidad": cantidad_boletas,
}

print(cesta_de_compra)
print(list(nombre_sector.keys()))
