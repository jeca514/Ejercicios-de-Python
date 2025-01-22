def convertir_divisa(monto, tasa_cambio):
    return monto * tasa_cambio

def main():
    """
    Función principal que ejecuta el programa de conversión de divisas.
    El programa permite convertir entre Pesos Colombianos, Dólares y Euros
    utilizando tasas de cambio ficticias. Presenta un menú interactivo para
    seleccionar la operación deseada.
    Menú de opciones:
    1. Convertir Divisas: Permite al usuario seleccionar la divisa de origen,
       ingresar el monto a convertir y seleccionar la divisa de destino.
       Luego, muestra el monto convertido.
    2. Salir: Termina la ejecución del programa.
    El programa sigue ejecutándose hasta que el usuario elija la opción de salir.
    Raises:
        ValueError: Si el usuario ingresa una opción no válida en el menú o
                    un valor no numérico para las opciones y montos.
    """
    # Nombres de las divisas
    divisas = ["Pesos Colombianos", "Dólares", "Euros"]
    
    # Asignamos las tasas de cambio (valores ficticios)
    tasa_cambio = [
        [1, 0.00026, 0.00023],  # COP a COP, USD, EUR
        [3800, 1, 0.88],        # USD a COP, USD, EUR
        [4300, 1.14, 1]         # EUR a COP, USD, EUR
    ]
    
    while True:
        # Mostrar menú
        print("Menú de Convertir Divisas")
        print("   1. Convertir Divisas")
        print("   2. Salir")
        
        # Ingresar una opción
        op = int(input("Elija una opción (1-2): "))
        
        if op == 1:
            # Elegir divisas
            print("¿Qué divisa tiene?")
            print("   1. Pesos Colombianos")
            print("   2. Dólares")
            print("   3. Euros")
            d_origen = int(input()) - 1  # Convertir a índice 0-based

            # Elegir Monto
            monto = float(input("¿Cuánto dinero tiene? "))

            # Elegir divisa destino
            print("¿Qué divisa quiere?")
            print("   1. Pesos Colombianos")
            print("   2. Dólares")
            print("   3. Euros")
            d_salida = int(input()) - 1  # Convertir a índice 0-based
            
            # Calcular conversión
            monto_convertido = convertir_divisa(monto, tasa_cambio[d_origen][d_salida])
            
            # Mostrar resultado
            print(f"Sus {monto} {divisas[d_origen]} son {monto_convertido} {divisas[d_salida]}")
        
        elif op == 2:
            print("Gracias, vuelva pronto")
            break
        
        else:
            print("Opción no válida")
        
        input("Presione enter para continuar")

if __name__ == "__main__":
    main()
