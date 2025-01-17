"""Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

import time

while True:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero < 0:
            print("El número tiene que ser positivo.")
        else:
            break
    except ValueError:
        print("El valor introducido no es un número entero")

for i in range(
    numero, -1, -1
):  # el primer -1 es para que vaya de uno en uno, el segundo -1 es para que vaya de mayor a menor
    print(
        i, end=", ", flush=True
    )  # flush=True para que balla mostrando los numeros en tiempo real
    time.sleep(0.5)
