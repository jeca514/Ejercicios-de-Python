# codico fibonacci con recursividad y decorador cache
import time
import math
from functools import cache  # importo la funcion cache de functools


@cache  # decorador sobre cache para que guarde los valores de cada iteración de la funcion
def fibonacci_recurivo(n):
    return (
        n if n <= 1 else fibonacci_recurivo(n - 1) + fibonacci_recurivo(n - 2)
    )  # funcion recursiva de fibonacci


"""grafica para explicar la recursividad de la funcion recursiva de fibonacci
fibonacci(5)
├── fibonacci(4)
│   ├── fibonacci(3)
│   │   ├── fibonacci(2)
│   │   │   ├── fibonacci(1)  -> 1
│   │   │   ├── fibonacci(0)  -> 0
│   │   ├── fibonacci(1)      -> 1
│   ├── fibonacci(2)
│       ├── fibonacci(1)      -> 1
│       ├── fibonacci(0)      -> 0
├── fibonacci(3)
    ├── fibonacci(2)
    │   ├── fibonacci(1)     -> 1
    │   ├── fibonacci(0)      -> 0
    ├── fibonacci(1)          -> 1

"""


def fibonacci_iterativo(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


def fibonacci_explicito(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2  # Definir psi
    return int((phi**n - psi**n) / math.sqrt(5))


n = int(input("Introduce un número entero positivo: "))
lista = {}

start_time = time.time()
resultado = fibonacci_iterativo(n)
end_time = time.time() - start_time
print(
    f"El resultado de fibonacci_iterativo({n}) es {resultado} y se ha tardado {end_time} segundos"
)
lista["fibonacci_iterativo"] = end_time

start_time = time.time()
resultado = fibonacci_recurivo(n)
end_time = time.time() - start_time
print(
    f"\nEl resultado de fibonacci_recurivo({n}) es {resultado} y se ha tardado {end_time} segundos"
)
lista["fibonacci_recurivo"] = end_time

start_time = time.time()
resultado = fibonacci_explicito(n)
end_time = time.time() - start_time
print(
    f"\nEl resultado de fibonacci_explicito({n}) es {resultado} y se ha tardado {end_time} segundos\n"
)
lista["fibonacci_explicito"] = end_time

# lista odernada por tiempo de ejecució

lista_ordenada = sorted(lista.items(), key=lambda x: x[1])
for clave, valor in lista_ordenada:
    print(f"{clave}: {valor}", end=", ")


"""Conclusión: la forma mas eficiente de calcular la serie de fibonacci es mediante la formula explicita,
pero tiene un problema, que es la perdida de precisión al calcular números muy grandes, por lo que la forma
en que se calculan las raices cuadradas y las potencias de los números, puede dar lugar a errores de redondeo

la mas precisa y eficiente para valores de pocos millones es la forma iterativa, ya que no tiene problema y 
la forma recursiva aunque interesante es la menos eficeinte y el @cache tiene un limite de 1000 valores
"""
