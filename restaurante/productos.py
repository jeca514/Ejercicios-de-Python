from abc import ABC, abstractmethod
from dataclasses import dataclass
import csv
import pandas as pd


# --- producto para la venta ---
@dataclass
class Producto:
    _nombre: str
    _precio: float
    _stock: int

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = stock

    def actualizar_stock(self, cantidad: int):
        nuevo_stock = self.stock + cantidad
        if nuevo_stock < 0:
            raise ValueError("No hay suficiente stock")
        self.stock = nuevo_stock


# --- clase para modificar inventario csv ---


class Inventario:
    @staticmethod
    def actualizar_stock(producto: Producto):
        """
        Actualiza el stock de un producto en el archivo csv
        """
        df = pd.read_csv("restaurante/inventario.csv")
        df.loc[df["nombre"] == producto.nombre, "stock"] = (
            producto.stock
        )  # df.loc permite acceder a un grupo de filas y columnas por etiqueta(s) o una matriz booleana.
        df.to_csv(
            "restaurante/inventario.csv", index=False
        )  # .to_csv convierte el DataFrame en un archivo csv y sobreescribe el archivo existente

    @staticmethod
    def actualizar_precio(producto: Producto):
        """
        Actualiza el precio de un producto en el archivo csv
        """
        df = pd.read_csv("restaurante/inventario.csv")
        df.loc[df["nombre"] == producto.nombre, "precio"] = producto.precio
        df.to_csv("restaurante/inventario.csv", index=False)

    @staticmethod
    def agregar_producto(producto: Producto):
        """
        Agrega un producto al archivo csv
        """
        df = pd.read_csv("restaurante/inventario.csv")
        if producto.nombre in df["nombre"].values:
            raise ValueError("El producto ya existe en el inventario")
        df = df.append(
            {
                "nombre": producto.nombre,
                "precio": producto.precio,
                "stock": producto.stock,
            },
        )


# ---  objeto comprable ---
class Comprable(ABC):
    @abstractmethod
    def validar(self) -> bool:  # funcion que valida las condiciones de compra
        pass


# --- clase para vender productos ---
@dataclass
class Compra(Comprable):
    _producto: Producto
    _cantidad: int

    @property
    def producto(self):
        return self._producto

    @property
    def cantidad(self):
        return self._cantidad

    def validar(self) -> bool:  # valida la cantidad de productos en stock
        if self.producto.stock < self.cantidad:
            return False
        return True

    def procesar_compra(self):  # actualiza el stock del producto
        if not self.validar():
            raise ValueError("No hay suficiente stock")
        self.producto.actualizar_stock(
            -self.cantidad
        )  # resta la cantidad comprada al stock
        Inventario.actualizar_stock(
            self.producto
        )  # actualiza el stock en el archivo csv
        return f"Compra exitosa. Nuevo stock de {self.producto.nombre}: {self.producto.stock}"


# --- menu para comprar productos ---
def menu_compra(productos: list):
    print("\n--- Menú de productos ---")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto.nombre} - ${producto.precio} - Stock: {producto.stock}")
    compra = input("\nSeleccione el producto: ")
    cantidad = int(input("Cantidad: "))
    return productos[int(compra) - 1], cantidad


# --- uso ---

if __name__ == "__main__":
    df = pd.read_csv("restaurante/inventario.csv")
    productos = [
        Producto(row["nombre"], row["precio"], row["stock"])
        for index, row in df.iterrows()  # for index, row in df.iterrows() itera sobre las filas del DataFrame
    ]
    producto, cantidad = menu_compra(productos)
    compra = Compra(producto, cantidad)
    print(compra.procesar_compra())
    print("Inventario actualizado")
