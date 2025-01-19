from banco.clientes import Cuenta
from banco.funcionarios import Trabajadores

# Crear cuentas
cuenta1 = Cuenta("Jose Antonio Perez Chacon", 100000.0, "COP$")
cuenta2 = Cuenta("Maria Fernanda Lopez", 50000.0, "COP$")

# Mostrar detalles de la primera cuenta
cuenta1.mostrar_detalles_cuenta()

# Realizar operaciones en la cuenta 1
# Realizar un depósito
print("Realizando depósito de 25,000...")
resultado, mensaje = cuenta1.depositar(25000)
print(mensaje)
cuenta1.mostrar_detalles_cuenta()

# Realizar un retiro
print("Realizando retiro de 5,000...")
resultado, mensaje = cuenta1.retiro(5000)
print(mensaje)
cuenta1.mostrar_detalles_cuenta()


# Mostrar detalles de la segunda cuenta
cuenta2.mostrar_detalles_cuenta()

# Realizar una transacción entre cuentas
print("Realizando una transacción de 15,000 de la cuenta 1 a la cuenta 2...")
resultado, mensaje = cuenta1.transaccion(15000, cuenta2)
print(mensaje)
cuenta1.mostrar_detalles_cuenta()
cuenta2.mostrar_detalles_cuenta()

cuenta3 = Cuenta("andrea Fernanda Lopez", "mil pesos", "COP$")
cuenta3.mostrar_detalles_cuenta()


print("\n============== Empleados ==============")

empleado = Trabajadores("Tomas Lucas Pachon", 1500000, 3)
empleado.mostrar_detalles_empleado()

empleado.rendimiento = 5

empleado.mostrar_detalles_empleado()
