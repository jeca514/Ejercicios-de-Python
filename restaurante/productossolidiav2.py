from sqlmodel import Session, select
from models import Producto, Venta, DetalleVenta, Cliente
from database import engine


# ---------------------------
# Repositorios
# ---------------------------
class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, producto: Producto) -> Producto:
        self.session.add(producto)
        return producto

    def get_by_id(self, producto_id: int) -> Producto:
        return self.session.get(Producto, producto_id)

    def get_by_name(self, name: str) -> Producto:
        return self.session.exec(
            select(Producto).where(Producto.nombre == name)
        ).first()

    def get_all(self) -> list[Producto]:
        return self.session.exec(select(Producto)).all()

    def update_stock(self, producto: Producto, cantidad: int) -> None:
        producto.stock += cantidad
        self.session.add(producto)

    def update_price(self, producto: Producto, nuevo_precio: float) -> None:
        producto.precio = nuevo_precio
        self.session.add(producto)

    def delete(self, producto: Producto) -> None:
        self.session.delete(producto)


class ClientRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_or_create_anonymous(self) -> Cliente:
        cliente = self.session.exec(
            select(Cliente).where(Cliente.identificacion == "ANONIMO")
        ).first()

        if not cliente:
            cliente = Cliente(
                identificacion="ANONIMO", nombre="Cliente Anónimo", email="", celular=0
            )
            self.session.add(cliente)
        return cliente

    def get_by_cedula(self, cedula: str) -> Cliente:
        return self.session.get(Cliente, cedula)

    def create(self, cliente: Cliente) -> Cliente:
        self.session.add(cliente)
        return cliente


class SaleRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_venta(self) -> Venta:
        venta = Venta()
        self.session.add(venta)
        return venta

    def create_detalle(self, detalle: DetalleVenta) -> DetalleVenta:
        self.session.add(detalle)
        return detalle

    def get_detalles(self, venta_id: int) -> list[DetalleVenta]:
        return self.session.exec(
            select(DetalleVenta).where(DetalleVenta.venta_id == venta_id)
        ).all()


# ---------------------------
# Servicio de Ventas
# ---------------------------
class SaleService:
    def __init__(self):
        self.session = Session(engine)
        self.product_repo = ProductRepository(self.session)
        self.client_repo = ClientRepository(self.session)
        self.sale_repo = SaleRepository(self.session)

    def process_sale(self):
        try:
            venta = self.sale_repo.create_venta()
            self._handle_products_selection(venta)
            self._process_client_association(venta)
            self._finalize_sale(venta)
        except Exception as e:
            self.session.rollback()
            print(f"Error: {str(e)}")
        finally:
            self.session.close()

    def _handle_products_selection(self, venta: Venta):
        while True:
            self._show_products()
            producto = self._select_product()
            if not producto:
                break

            cantidad = self._get_valid_quantity(producto)
            if not cantidad:
                continue

            self._add_to_cart(venta, producto, cantidad)

    def _show_products(self):
        productos = self.product_repo.get_all()
        for p in productos:
            status = f"${p.precio} (Stock: {p.stock})" if p.stock > 0 else "AGOTADO"
            print(f"{p.id}. {p.nombre.ljust(20)} {status}")

    def _select_product(self):
        choice = input("\nSeleccione producto (ID) o 'q' para terminar: ").strip()
        if choice.lower() == "q":
            return None

        try:
            producto = self.product_repo.get_by_id(int(choice))
            return producto if producto else print("ID inválido")
        except ValueError:
            print("Entrada inválida")
            return None

    def _get_valid_quantity(self, producto: Producto):
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("Cantidad debe ser positiva")
                return None
            if cantidad > producto.stock:
                print("Stock insuficiente")
                return None
            return cantidad
        except ValueError:
            print("Cantidad inválida")
            return None

    def _add_to_cart(self, venta: Venta, producto: Producto, cantidad: int):
        self.product_repo.update_stock(producto, -cantidad)
        detalle = DetalleVenta(
            venta_id=venta.id,
            producto_id=producto.id,
            cantidad=cantidad,
            precio=producto.precio,
        )
        self.sale_repo.create_detalle(detalle)
        print(f"{cantidad}x {producto.nombre} agregado(s)")

    def _process_client_association(self, venta: Venta):
        detalles = self.sale_repo.get_detalles(venta.id)
        cliente = self._get_client()
        for detalle in detalles:
            detalle.cliente_id = cliente.identificacion

    def _get_client(self) -> Cliente:
        cedula = input("\nCédula cliente (enter para anónimo): ").strip()
        if not cedula:
            return self.client_repo.get_or_create_anonymous()

        cliente = self.client_repo.get_by_cedula(cedula)
        if cliente:
            print(f"Cliente existente: {cliente.nombre}")
            return cliente

        return self._create_new_client(cedula)

    def _create_new_client(self, cedula: str) -> Cliente:
        nombre = input("Nombre completo: ").strip() or "Cliente Anónimo"
        email = input("Email: ").strip()
        celular = input("Celular: ").strip() or 0
        nuevo_cliente = Cliente(
            identificacion=cedula, nombre=nombre, email=email, celular=celular
        )
        return self.client_repo.create(nuevo_cliente)

    def _finalize_sale(self, venta: Venta):
        self._show_sale_summary(venta)
        if input("\nConfirmar compra (s/n)? ").lower() == "s":
            self.session.commit()
            print("Venta confirmada!")
        else:
            self.session.rollback()
            print("Venta cancelada")

    def _show_sale_summary(self, venta: Venta):
        detalles = self.sale_repo.get_detalles(venta.id)
        total = sum(d.cantidad * d.precio for d in detalles)

        print("\nResumen de compra:")
        for d in detalles:
            producto = self.product_repo.get_by_id(d.producto_id)
            print(f"{producto.nombre.ljust(20)} {d.cantidad}x ${d.precio:.2f}")
        print(f"\nTOTAL: ${total:.2f}")


# ---------------------------
# Punto de entrada
# ---------------------------
if __name__ == "__main__":
    sale_system = SaleService()
    sale_system.process_sale()
