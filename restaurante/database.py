from sqlmodel import create_engine, SQLModel
from models import Producto, Venta, DetalleVenta

engine = create_engine(
    "mysql+mariadbconnector://app_user:Password123!@127.0.0.1:3306/restaurante",
    echo=False,
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
