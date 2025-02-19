from abc import ABC, abstractmethod
from enum import Enum


# --- 1. Enum (menú de opciones) ---
class TipoPago(Enum):
    EFECTIVO = "efectivo"
    TARJETA = "tarjeta"
    PAYPAL = "paypal"


# --- 2. Clase Abstracta (SOLID) ---
class MetodoDePago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> bool:
        pass


# --- 3. Clases Concretas ---
class Efectivo(MetodoDePago):
    def procesar_pago(self, monto: float) -> bool:
        print("Pagando en efectivo")
        return True


class Tarjeta(MetodoDePago):
    def procesar_pago(self, monto: float) -> bool:
        print("Pagando con tarjeta")
        return True


class PayPal(MetodoDePago):
    def procesar_pago(self, monto: float) -> bool:
        print("Pagando con PayPal")
        return True


# --- 4. Fábrica Simple ---
class PaymentMethodFactory:
    _registry = {
        TipoPago.EFECTIVO: Efectivo,
        TipoPago.TARJETA: Tarjeta,
        TipoPago.PAYPAL: PayPal,
    }

    @staticmethod
    def crear(tipo: TipoPago) -> MetodoDePago:
        return PaymentMethodFactory._registry[tipo]()


# --- 5. menú---
def opciones_de_pago():
    print("\n--- Opciones de pago ---")
    for i, opcion in enumerate(TipoPago, start=1):
        print(f"{i}. {opcion.name}")
    pago = input("\nSelecione el metodo de pago: ")
    return list(TipoPago)[int(pago) - 1]


# --- 6. Uso ---

if __name__ == "__main__":
    metodo = opciones_de_pago()
    print(metodo)
    pago = PaymentMethodFactory.crear(metodo)
    pago.procesar_pago(100.50)  # Output: "Pagando en efectivo"
