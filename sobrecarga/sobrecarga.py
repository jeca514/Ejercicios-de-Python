# Diferentes tipos de sobrecarga de operadores
# 
# La sobrecarga de operadores es una característica de los lenguajes de programación que permite definir el comportamiento de los operadores en clases personalizadas. En Python, la sobrecarga de operadores se logra mediante la definición de métodos especiales en una clase. Los métodos especiales son aquellos que tienen doble guion bajo al inicio y al final de su nombre. 
# 
# En Python, la sobrecarga de operadores se logra mediante la definición de métodos especiales en una clase. Por ejemplo, si queremos sobrecargar el operador suma (+) en una clase, debemos definir el método __add__ en la clase. 
# 
# A continuación, se muestra un ejemplo de cómo sobrecargar el operador suma en una clase llamada Numero. En este caso, el operador suma realiza la suma de los atributos valor de dos instancias de la clase Numero.
# 
# class Numero:
#     def __init__(self, valor):
#         self.valor = valor
# 
#     def __add__(self, otro_numero):
#         return self.valor + otro_numero.valor
# 
# numero1 = Numero(5)
# numero2 = Numero(10)
# resultado = numero1 + numero2
# print(resultado)  # Output: 15
# En este ejemplo, la clase Numero tiene un atributo valor y un método especial __add__ que sobrecarga el operador suma (+). Cuando se suman dos instancias de la clase Numero, el método __add__ se ejecuta y devuelve la suma de los atributos valor de ambas instancias. 
# 
# Además del operador suma, Python permite sobrecargar otros operadores, como resta (-), multiplicación (*), división (/), igualdad (==), entre otros. Para sobrecargar un operador en Python, se debe definir el método especial correspondiente en la clase. A continuación, se muestran algunos ejemplos de métodos especiales y su correspondencia con los operadores:
# 
# Operador	Método especial
# +	__add__
# -	__sub__
# *	__mul__
# /	__truediv__
# //	__floordiv__
# %	__mod__
# **	__pow__
# <
"""
Sobrecarga de operadores

La sobrecarga de operadores es una característica de los lenguajes de programación 
que permite definir el comportamiento de los operadores en clases personalizadas. 
En Python, la sobrecarga de operadores se logra mediante la definición de métodos especiales
en una clase.
"""
from math import number

def __add__(int, int):
    return int + int