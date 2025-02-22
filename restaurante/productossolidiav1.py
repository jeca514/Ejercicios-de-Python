from sqlmodel import Session, select
from models import Producto, Venta, DetalleVenta, Cliente
from database import engine


# Gestor de sesiones de base de datos
class DatabaseSessionManager:
    def __init__(self, engine):
        self.engine = engine

    def get_session(self):
        return Session(self.engine)


# Repositorio para operaciones con Producto
class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_product(self, producto: Producto) -> Producto:
        self.session.add(producto)
        self.session.commit()
        self.session.refresh(producto)
        return producto

    def get_by_name(self, nombre: str) -> Producto:
        statement = select(Producto).where(Producto.nombre == nombre)
        result = self.session.exec(statement)
        return result.one_or_none()

    def update_stock(self, nombre: str, cantidad: int) -> Producto:
        producto = self.get_by_name(nombre)
        if not producto:
            raise ValueError(f"Producto con nombre '{nombre}' no encontrado.")
        producto.stock += cantidad
        self.session.add(producto)
        self.session.commit()
        self.session.refresh(producto)
        return producto

    def update_price(self, nombre: str, nuevo_precio: float) -> Producto:
        producto = self.get_by_name(nombre)
        if not producto:
            raise ValueError(f"Producto con nombre '{nombre}' no encontrado.")
        producto.precio = nuevo_precio
        self.session.add(producto)
        self.session.commit()
        self.session.refresh(producto)
        return producto

    def delete_product(self, nombre: str):
        producto = self.get_by_name(nombre)
        if not producto:
            raise ValueError(f"Producto con nombre '{nombre}' no encontrado.")
        self.session.delete(producto)
        self.session.commit()

    def list_products(self):
        statement = select(Producto)
        result = self.session.exec(statement)
        return result.all()


# Repositorio para operaciones de Venta y DetalleVenta
class SaleRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_last_sale_id(self) -> int:
        statement = select(Venta).order_by(Venta.id.desc())
        result = self.session.exec(statement)
        ultimo_registro = result.first()
        return ultimo_registro.id if ultimo_registro else 0

    def create_provisional_sale(self) -> Venta:
        venta = Venta()
        self.session.add(venta)
        self.session.flush()  # Se asigna un id sin confirmar la transacción
        return venta

    def add_sale_detail(self, detalle: DetalleVenta):
        self.session.add(detalle)

    def get_sale_details(self, venta_id: int):
        statement = select(DetalleVenta).where(DetalleVenta.venta_id == venta_id)
        result = self.session.exec(statement)
        return result.all()


# Repositorio para operaciones con Cliente
class CustomerRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_anonymous(self) -> Cliente:
        statement = select(Cliente).where(Cliente.identificacion == "ANONIMO")
        result = self.session.exec(statement)
        cliente = result.first()
        if not cliente:
            cliente = Cliente(
                identificacion="ANONIMO", nombre="Cliente Anónimo", email="", celular=0
            )
            self.session.add(cliente)
            self.session.flush()
            self.session.refresh(cliente)
        return cliente

    def get_by_identification(self, identificacion: str) -> Cliente:
        return self.session.get(Cliente, identificacion)

    def add_customer(self, cliente: Cliente) -> Cliente:
        self.session.add(cliente)
        self.session.flush()
        self.session.refresh(cliente)
        return cliente


# Lógica de negocio para la venta
class SaleService:
    def __init__(self, session: Session):
        self.session = session
        self.product_repo = ProductRepository(session)
        self.sale_repo = SaleRepository(session)
        self.customer_repo = CustomerRepository(session)

    def add_product_to_sale(self, venta: Venta, producto_id: int, cantidad: int):
        producto = self.session.get(Producto, producto_id)
        if not producto:
            raise ValueError("Producto no encontrado.")
        if not producto.stock or producto.stock < cantidad:
            raise ValueError("Producto sin stock suficiente.")
        detalle = DetalleVenta(
            venta_id=venta.id,
            producto_id=producto.id,
            cantidad=cantidad,
            precio=producto.precio,
        )
        self.sale_repo.add_sale_detail(detalle)
        producto.stock -= cantidad
        self.session.flush()  # Actualiza los cambios sin confirmar
        return detalle

    def summarize_sale(self, venta: Venta) -> dict:
        detalles = self.sale_repo.get_sale_details(venta.id)
        resumen = {}
        total = 0
        for detalle in detalles:
            if detalle.producto_id in resumen:
                resumen[detalle.producto_id]["cantidad"] += detalle.cantidad
            else:
                resumen[detalle.producto_id] = {
                    "cantidad": detalle.cantidad,
                    "precio": detalle.precio,
                }
            total += detalle.cantidad * detalle.precio
        return {"detalles": resumen, "total": total}

    def confirm_sale(self, venta: Venta, cliente: Cliente):
        detalles = self.sale_repo.get_sale_details(venta.id)
        for detalle in detalles:
            detalle.cliente_id = cliente.identificacion
        self.session.commit()

    def cancel_sale(self):
        self.session.rollback()


# Interfaz de usuario para gestionar la venta
class SaleUI:
    def __init__(self, sale_service: SaleService):
        self.sale_service = sale_service

    def display_products(self):
        products = self.sale_service.product_repo.list_products()
        for producto in products:
            if producto.stock and producto.stock > 0:
                print(f"{producto.id}. {producto.nombre}, Precio: ${producto.precio}")
            else:
                print(f"{producto.id}. {producto.nombre}, Stock agotado")

    def run(self):
        venta = self.sale_service.sale_repo.create_provisional_sale()
        print(f"Venta provisional creada con id {venta.id}")

        while True:
            input("Presione Enter para continuar...")
            print("\n--- Agregar producto a la venta ---")
            print("Elija un producto de la lista:")
            self.display_products()

            opcion = input(
                "Ingrese el ID del producto a agregar (o 'q' para ir a paga): "
            )
            if opcion.lower() == "q":
                break

            try:
                producto_id = int(opcion)
            except ValueError:
                print("Entrada no válida. Intente nuevamente.")
                continue

            producto = self.sale_service.session.get(Producto, producto_id)
            if not producto:
                print("Producto no encontrado.")
                continue

            if not producto.stock or producto.stock <= 0:
                print("Producto sin stock disponible.")
                continue

            cantidad_input = input("Ingrese la cantidad a agregar: ")
            try:
                cantidad = int(cantidad_input)
            except ValueError:
                print("Cantidad no válida.")
                continue

            if cantidad > producto.stock:
                print("Cantidad solicitada supera el stock disponible.")
                continue

            try:
                self.sale_service.add_product_to_sale(venta, producto_id, cantidad)
                print(
                    f"Agregado {cantidad} unidades de '{producto.nombre}' a la venta {venta.id}."
                )
            except ValueError as e:
                print(e)

        resumen = self.sale_service.summarize_sale(venta)
        total_a_pagar = resumen["total"]
        print("\nResumen de la compra:")
        for prod_id, info in resumen["detalles"].items():
            producto = self.sale_service.session.get(Producto, prod_id)
            subtotal = info["cantidad"] * info["precio"]
            print(f"{producto.nombre:.<30} {info['cantidad']} x ${info['precio']:.2f}")
        print(f"{'':>20}Total a pagar: ${total_a_pagar:.2f}")

        cliente_input = input(
            "Ingrese la cédula del cliente para esta venta (o presione Enter para continuar sin datos): "
        )
        if cliente_input.strip() == "":
            print("No se proporcionó cédula. Se usará el cliente anónimo.")
            cliente = self.sale_service.customer_repo.get_anonymous()
        else:
            cedula = cliente_input.strip()
            cliente = self.sale_service.customer_repo.get_by_identification(cedula)
            if cliente:
                print(f"Cliente encontrado: {cliente.nombre}")
            else:
                print(
                    "Cliente no encontrado. Por favor, ingrese los siguientes datos para crear un nuevo cliente."
                )
                nombre = input("Nombre del cliente: ")
                email = input("Email: ")
                celular = input("Celular: ")
                if nombre.strip() == "":
                    print("No se proporcionó nombre. Se asignará 'Cliente Anónimo'.")
                    nombre = "Cliente Anónimo"
                cliente = Cliente(
                    identificacion=cedula, nombre=nombre, email=email, celular=celular
                )
                self.sale_service.customer_repo.add_customer(cliente)
                print(f"Cliente creado con cédula: {cliente.identificacion}")

        confirmar = input("¿Confirma la compra? (s/n): ")
        if confirmar.lower() == "s":
            self.sale_service.confirm_sale(venta, cliente)
            print("Compra confirmada.")
        else:
            self.sale_service.cancel_sale()
            print("Compra cancelada. Se han revertido los cambios.")


def main():
    session_manager = DatabaseSessionManager(engine)
    with session_manager.get_session() as session:
        sale_service = SaleService(session)
        sale_ui = SaleUI(sale_service)
        sale_ui.run()


if __name__ == "__main__":
    main()
