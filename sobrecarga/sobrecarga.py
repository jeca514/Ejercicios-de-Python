from functools import singledispatch


class Calculadora:
    @singledispatch
    def sumar(self, a, b):
        return a + b

    @sumar.register(int)
    def _(self, a: int, b: int):
        return a + b

    @sumar.register(float)
    def _(self, a: float, b: float):
        return a + b

    def sumar_tres(self, a, b, c):
        # Método adicional para manejar tres parámetros
        return a + b + c


calc = Calculadora()

# Usar el método sumar con dos enteros
resultado1 = calc.sumar(1, 2)
print(f"Resultado de sumar 1 y 2: {resultado1}")

# Usar el método sumar con tres enteros
resultado2 = calc.sumar_tres(1, 2, 3)  # Usar un método separado para tres parámetros
print(f"Resultado de sumar 1, 2 y 3: {resultado2}")

# Usar el método sumar con dos flotantes
resultado3 = calc.sumar(1.5, 2.5)
print(f"Resultado de sumar 1.5 y 2.5: {resultado3}")
