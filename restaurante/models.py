from sqlmodel import Field, SQLModel, Column, TIMESTAMP, text, Relationship


class Cliente(SQLModel, table=True):
    identificacion: str = Field(primary_key=True)
    nombre: str
    email: str | None = None
    celular: int | None = None


class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    stock: int | None = None
    precio: float | None = None
    detalles: list["DetalleVenta"] = Relationship(back_populates="producto")


class Venta(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    venta_fecha: str | None = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
        )
    )
    created_datetime: str | None = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
        )
    )
    updated_datetime: str | None = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
            server_onupdate=text("CURRENT_TIMESTAMP"),
        )
    )
    detalles: list["DetalleVenta"] = Relationship(back_populates="venta")


class DetalleVenta(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    venta_id: int | None = Field(default=None, foreign_key="venta.id")
    producto_id: int | None = Field(default=None, foreign_key="producto.id")
    cliente_id: str | None = Field(default=None, foreign_key="cliente.identificacion")
    cantidad: int | None = None
    precio: float | None = None
    venta: Venta | None = Relationship(back_populates="detalles")
    producto: Producto | None = Relationship(back_populates="detalles")
