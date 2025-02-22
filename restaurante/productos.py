# from sqlalchemy.engine import result
from sqlmodel import Session, select
from models import Producto, Venta, DetalleVenta, Cliente
from database import engine


# ---------------------------
# Funciones para Producto
# ---------------------------
def agregar_producto(producto):
    with Session(engine) as session:
        session.add(producto)
        session.commit()
        session.refresh(producto)
        return producto


def actualizar_stock(nombre_producto: str, cantidad: int):
    with Session(engine) as session:
        statement = select(Producto).where(Producto.nombre == nombre_producto)
        result = session.exec(statement)
        producto = result.one_or_none()
        if producto:
            producto.stock += cantidad
            session.add(producto)
            session.commit()
            session.refresh(producto)
            return producto
        else:
            print(f"Producto con nombre '{nombre_producto}' no encontrado.")
            return None


def actualizar_precio(nombre_producto: str, nuevo_precio: float):
    with Session(engine) as session:
        statement = select(Producto).where(Producto.nombre == nombre_producto)
        result = session.exec(statement)
        producto = result.one_or_none()
        if producto:
            producto.precio = nuevo_precio
            session.add(producto)
            session.commit()
            session.refresh(producto)
            return producto
        else:
            print(f"Producto con nombre '{nombre_producto}' no encontrado.")
            return None


def eliminar_producto(nombre_producto: str):
    with Session(engine) as session:
        statement = select(Producto).where(Producto.nombre == nombre_producto)
        result = session.exec(statement)
        producto = result.one_or_none()
        if producto:
            session.delete(producto)
            session.commit()
            print(f"Producto con nombre '{nombre_producto}' eliminado.")
        else:
            print(f"Producto con nombre '{nombre_producto}' no encontrado.")


def mostrar_productos():
    with Session(engine) as session:
        statement = select(Producto)
        result = session.exec(statement)
        productos = result.all()
        for producto in productos:
            if producto.stock and producto.stock > 0:
                print(f"{producto.id}. {producto.nombre},  Precio: ${producto.precio}")
            else:
                print(f"{producto.id}. {producto.nombre}, Stock agotado")


# ---------------------------
# Funciones para Venta y DetalleVenta
# ---------------------------
def obtener_ultimo_id_venta():
    with Session(engine) as session:
        statement = select(Venta).order_by(Venta.id.desc())
        result = session.exec(statement)
        ultimo_registro = result.first()
        if ultimo_registro:
            return ultimo_registro.id
        else:
            print("La tabla está vacía")
            return 0


def crear_venta_provisional() -> Venta:
    session = Session(engine)
    venta = Venta()
    session.add(venta)
    session.flush()  # Se asigna un id a la venta sin confirmar la transacción
    print(f"Venta provisional creada con id {venta.id}")
    return (
        venta,
        session,
    )  # Retornamos la venta y la sesión abierta para seguir trabajando


def obtener_cliente_anonimo(session: Session) -> Cliente:
    # Buscar un cliente anónimo existente con identificacion "ANONIMO"
    cliente = session.exec(
        select(Cliente).where(Cliente.identificacion == "ANONIMO")
    ).first()
    if not cliente:
        cliente = Cliente(
            identificacion="ANONIMO", nombre="Cliente Anónimo", email="", celular=0
        )
        session.add(cliente)
        session.flush()
        session.refresh(cliente)
    return cliente


def canasta_venta():
    # Creamos la venta provisional y obtenemos la sesión activa
    venta_actual, session = crear_venta_provisional()
    try:
        opcion = ""
        while opcion.lower() != "q":
            input("Presione Enter para continuar...")
            print("\n--- Agregar producto a la venta ---")
            print("Elija un producto de la lista:")
            mostrar_productos()

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

            producto = session.get(Producto, producto_id)
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

            # Crear el detalle de venta vinculado con la venta provisional
            detalle = DetalleVenta(
                venta_id=venta_actual.id,
                producto_id=producto.id,
                cantidad=cantidad,
                precio=producto.precio,
            )
            session.add(detalle)
            # Actualizar el stock del producto
            producto.stock -= cantidad
            session.flush()  # Enviamos los cambios sin confirmar la transacción
            print(
                f"Agregado {cantidad} unidades de '{producto.nombre}' a la venta {venta_actual.id}."
            )

        # Agrupar detalles de venta por producto_id
        detalle_agrupado = {}
        for detalle in session.exec(
            select(DetalleVenta).where(DetalleVenta.venta_id == venta_actual.id)
        ).all():
            if detalle.producto_id in detalle_agrupado:
                detalle_agrupado[detalle.producto_id]["cantidad"] += detalle.cantidad
            else:
                detalle_agrupado[detalle.producto_id] = {
                    "cantidad": detalle.cantidad,
                    "precio": detalle.precio,
                }

        total_a_pagar = 0
        print("\nResumen de la compra:")
        for prod_id, info in detalle_agrupado.items():
            producto = session.get(Producto, prod_id)
            subtotal = info["cantidad"] * info["precio"]
            total_a_pagar += subtotal
            print(f"{producto.nombre:.<30} {info['cantidad']} x ${info['precio']:.2f}")
        print(f"{'':>20}Total a pagar: ${total_a_pagar:.2f}")

        # Solicitar la cédula del cliente
        cliente_input = input(
            "Ingrese la cédula del cliente para esta venta (o presione Enter para continuar sin datos): "
        )
        if cliente_input.strip() == "":
            print("No se proporcionó cédula. Se usará el cliente anónimo.")
            cliente = obtener_cliente_anonimo(session)
            cliente_id = cliente.identificacion
        else:
            cedula = cliente_input.strip()
            cliente = session.get(Cliente, cedula)
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
                session.add(cliente)
                session.flush()
                session.refresh(cliente)
                print(f"Cliente creado con cédula: {cliente.identificacion}")
            cliente_id = cliente.identificacion

        # Actualizar los detalles de venta con el cliente_id obtenido
        detalles = session.exec(
            select(DetalleVenta).where(DetalleVenta.venta_id == venta_actual.id)
        ).all()
        for detalle in detalles:
            detalle.cliente_id = cliente_id

        confirmar = input("¿Confirma la compra? (s/n): ")
        if confirmar.lower() == "s":
            session.commit()
            print("Compra confirmada.")
        else:
            session.rollback()
            print("Compra cancelada. Se han revertido los cambios.")
    finally:
        session.close()


if __name__ == "__main__":
    canasta_venta()
