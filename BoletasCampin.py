"""Realizar un programa en Python que calcule el total a pagar en entradas al estadio el CAMPIN.
El estadio cuenta con los siguientes sectores codificados y sus respectivos precios:
Sectores del estadio
A- Norte alta $15.000
B- Norte baja $13.000
C- Oriental alta $10.000
D- Occidental alta $11.000
E- Exclusivo $20.000

El programa debe imprimir:
• Precio Unitario de la boleta
• Cantidad de entradas compradas
• Total a pagar Nota: Validar que la cantidad de boletas debe ser un entero positivo.
"""

# Diccionario de lista de boletas
lista_boletas = {
    "A": {"nombre": "Norte alta", "precio": 15000},
    "B": {"nombre": "Norte baja", "precio": 13000},
    "C": {"nombre": "Oriental alta", "precio": 10000},
    "D": {"nombre": "Occidental alta", "precio": 11000},
    "E": {"nombre": "Exclusivo", "precio": 20000},
}


# funcion que tiene la logica de procesar la cesta de compras
def Compra_boletas(lista_boletas):
    opcion = 0
    cesta_de_compra = {}  # Diccionario que hara de cache
    opciones = list(lista_boletas.keys())
    while opcion != 6:  # bucle que no se cansela hasta que se de la opcion salir
        opcion = int(
            input(
                "Seleccione el sector de la boleta que desea comprar: \n"
                "1. Norte alta\n"
                "2. Norte baja\n"
                "3. Oriental alta\n"
                "4. Occidental alta\n"
                "5. Exclusivo\n"
                "6. Salir\n"
                "Opcion: "
            )
        )
        if opcion != 6:  # if para agregar los elementos en la cesta de compra
            while True:
                try:  # pide el numero de boletas
                    cantidad_boletas = int(
                        input("Introduce la cantidad de boletas que desea comprar: ")
                    )
                    if cantidad_boletas < 0:
                        print("El número tiene que ser positivo.")
                    else:  # si la cantidad de boletas es valida agrega los datos a la cesta de compras
                        clave = opciones[opcion - 1]
                        cesta_de_compra[lista_boletas[clave]["nombre"]] = {
                            "precio": lista_boletas[clave]["precio"],
                            "cantidad_boletas": cantidad_boletas,
                        }
                        break

                except ValueError:
                    print("El valor introducido no es un número entero")

            print("\nCesta actual:")
            total = 0
            totalboletas = 0
            for sector, detalles in cesta_de_compra.items():
                subtotal = detalles["precio"] * detalles["cantidad_boletas"]
                subtotalboletas = detalles["cantidad_boletas"]
                total += subtotal
                totalboletas += subtotalboletas
                print(
                    f"- {sector}: {detalles['cantidad_boletas']} boletas x ${detalles['precio']} = ${subtotal}"
                )
            print(f"Total actual: ${total}\n")

            continuar = input("¿Desea comprar más boletas? (s/n): ").strip().lower()
            if continuar == "n":
                print("Gracias por su compra. Finalizando...")
                break

    print("\nResumen final de su compra:")
    total = 0
    totalboletas = 0
    for sector, detalles in cesta_de_compra.items():
        subtotal = detalles["precio"] * detalles["cantidad_boletas"]
        subtotalboletas = detalles["cantidad_boletas"]
        total += subtotal
        totalboletas += subtotalboletas
        print(
            f"- {sector}: {detalles['cantidad_boletas']} boletas x ${detalles['precio']} = ${subtotal}"
        )
    print(f"Total a pagar por {totalboletas} boletas: ${total}")


Compra_boletas(lista_boletas)
