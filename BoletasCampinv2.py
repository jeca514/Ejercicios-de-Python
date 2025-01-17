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


def obtener_opcion():
    while True:
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
            if opcion in range(1, 7):
                return opcion
            print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("El valor introducido no es un número entero")


def obtener_cantidad_boletas():
    while True:
        try:
            cantidad_boletas = int(
                input("Introduce la cantidad de boletas que desea comprar: ")
            )
            if cantidad_boletas > 0:
                return cantidad_boletas
            print("El número tiene que ser positivo.")
        except ValueError:
            print("El valor introducido no es un número entero")


def desea_continuar():
    while True:
        continuar = input("¿Desea comprar más boletas? (s/n): ").strip().lower()
        if continuar in ["s", "n"]:
            return continuar == "s"  # si es n returna false
        print("Opción no válida.")


def compra_boletas(lista_boletas):
    cesta_de_compra = {}
    opciones = list(lista_boletas.keys())
    while True:
        opcion = obtener_opcion()
        if opcion == 6:
            break

        cantidad_boletas = obtener_cantidad_boletas()
        clave = opciones[opcion - 1]
        nombre_sector = lista_boletas[clave]["nombre"]

        if nombre_sector in cesta_de_compra:
            cesta_de_compra[nombre_sector]["cantidad_boletas"] += cantidad_boletas
        else:
            cesta_de_compra[nombre_sector] = {
                "precio": lista_boletas[clave]["precio"],
                "cantidad_boletas": cantidad_boletas,
            }

        mostrar_cesta(cesta_de_compra)
        if not desea_continuar():  # cuando es n esto es True
            print("Gracias por su compra. Finalizando...")
            break

    resumen_final(cesta_de_compra)


compra_boletas(lista_boletas)
