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


def mostrar_cesta(cesta_de_compra):
    total = 0
    total_boletas = 0
    print("\nCesta actual:")
    for sector, detalles in cesta_de_compra.items():
        subtotal = detalles["precio"] * detalles["cantidad_boletas"]
        total += subtotal
        total_boletas += detalles["cantidad_boletas"]
        print(
            f"- {sector}: {detalles['cantidad_boletas']} boletas x ${detalles['precio']} = ${subtotal}"
        )
    print(f"Total actual: ${total}\n")
    return total, total_boletas


def resumen_final(cesta_de_compra):
    total = 0
    total_boletas = 0
    print("\nResumen final de su compra:")
    for sector, detalles in cesta_de_compra.items():
        subtotal = detalles["precio"] * detalles["cantidad_boletas"]
        total += subtotal
        total_boletas += detalles["cantidad_boletas"]
        print(
            f"- {sector}: {detalles['cantidad_boletas']} boletas x ${detalles['precio']} = ${subtotal}"
        )
    print(f"Total a pagar por {total_boletas} boletas: ${total}")


def compra_boletas(lista_boletas):
    opcion = 0
    cesta_de_compra = {}
    opciones = list(lista_boletas.keys())
    while opcion != 6:
        try:
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
            if opcion == 6:
                break
            if opcion not in range(1, 7):
                print("Opción no válida. Intente de nuevo.")
                continue

            while True:
                try:
                    cantidad_boletas = int(
                        input("Introduce la cantidad de boletas que desea comprar: ")
                    )
                    if cantidad_boletas < 0:
                        print("El número tiene que ser positivo.")
                    else:
                        clave = opciones[opcion - 1]
                        cesta_de_compra[lista_boletas[clave]["nombre"]] = {
                            "precio": lista_boletas[clave]["precio"],
                            "cantidad_boletas": cantidad_boletas,
                        }
                        break
                except ValueError:
                    print("El valor introducido no es un número entero")

            total, total_boletas = mostrar_cesta(cesta_de_compra)
            continuar = input("¿Desea comprar más boletas? (s/n): ").strip().lower()
            if continuar == "n":
                print("Gracias por su compra. Finalizando...")
                break

        except ValueError:
            print("El valor introducido no es un número entero")

    resumen_final(cesta_de_compra)


compra_boletas(lista_boletas)

"""
He dividido el código en funciones más pequeñas para mejorar la claridad y legibilidad. Ahora hay funciones separadas para mostrar la cesta actual y el resumen final de la compra. Además, he añadido algunas validaciones adicionales para manejar entradas no válidas.
"""
