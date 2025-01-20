class Cuenta:
    def __init__(self, titular, saldo, divisa):
        self._titular = titular
        self._divisa = divisa
        if isinstance(saldo, float):
            self._saldo = saldo
        else:
            print("saldo no valido se establecera en 0")
            self._saldo = 0

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo_nuevo):
        if isinstance(saldo_nuevo, (float, int)) and saldo_nuevo > 0:
            self._saldo = saldo_nuevo
        else:
            raise ValueError("Saldo inválido: debe ser un número flotante positivo.")

    @property
    def divisa(self):
        return self._divisa

    def depositar(self, monto_deposito):
        try:
            if monto_deposito > 0:
                self.saldo += monto_deposito
                return True, f"Depósito exitoso. Nuevo saldo: {self.saldo}"
            else:
                raise ValueError("El monto debe ser positivo.")
        except ValueError as e:
            return False, str(e)

    def retiro(self, monto_retiro):
        if (
            monto_retiro > 0 and monto_retiro <= self.saldo
        ):  # Usamos _saldo para evitar el setter
            self.saldo -= monto_retiro
            return True, f"Retiro exitoso. Nuevo saldo: {self.saldo}"
        elif monto_retiro > self.saldo:
            return False, "Fondos insuficientes"
        else:
            return False, "Valor inválido"

    def transaccion(self, monto_tran, cuenta_destino):
        if self.saldo >= monto_tran and monto_tran > 0:
            cuenta_destino.saldo += monto_tran
            self.saldo -= monto_tran
            return (
                True,
                f"Transacción exitosa. Nuevo saldo de {self.titular}: {self.saldo} y saldo de {cuenta_destino.titular}: {cuenta_destino.saldo}",
            )
        elif monto_tran > self.saldo:
            return False, "Fondos insuficientes"
        else:
            return False, "Valor inválido"

    def mostrar_detalles_cuenta(self):
        print("\n=== Detalles de la Cuenta ===")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo} {self.divisa}")
        print("=============================\n")


if __name__ == "__main__":
    # Crea una instancia de la clase Cuenta y la guarda en una variable
    cuenta = Cuenta("Jose Antonio Perez Chacon", 100000.0, "COP$")

    # Imprime las propiedades de la instancia
    print("Titular:", cuenta.titular)
    print("Saldo:", cuenta.saldo)
    print("Divisa:", cuenta.divisa)
    
    # Modificar saldo
    cuenta.saldo = 2000000
    cuenta.mostrar_detalles_cuenta()

    # Realizar un deposito
    resultado, mensaje = cuenta.depositar(25000)
    print(mensaje)
    print("Saldo final", cuenta.saldo)

    # Realiza un retiro
    resultado, mensaje = cuenta.retiro(5000)
    print(mensaje)
    print("Saldo final:", cuenta.saldo)
    
    
