def convertir_divisa(monto, tasa_cambio):
    return monto * tasa_cambio

def main():
    """
    Función principal para convertir divisas basadas en tasas de cambio predefinidas.
    Esta función presenta un menú al usuario con las siguientes opciones:
    1. Convertir divisas
    2. Salir
    Si el usuario elige convertir divisas, se le pedirá:
    1. Seleccionar la divisa que tiene (Pesos Colombianos, Dólares, Euros).
    2. Ingresar la cantidad de dinero que tiene.
    3. Seleccionar la divisa a la que quiere convertir (Pesos Colombianos, Dólares, Euros).
    La función calculará la cantidad convertida basada en las tasas de cambio predefinidas y mostrará el resultado.
    Si el usuario elige salir, el programa mostrará un mensaje de despedida y terminará.
    Si se selecciona una opción no válida, se mostrará un mensaje de error.
    La función continuará solicitando al usuario hasta que elija salir.
    """
    # Diccionario de divisas
    divisas = {
        1: "Pesos Colombianos",
        2: "Dólares",
        3: "Euros"
    }
    
    # Diccionario de tasas de cambio
    tasa_cambio = {
        (1, 1): 1,          # 1 COP a COP
        (1, 2): 0.00026,    # 1 COP a USD
        (1, 3): 0.00023,    # 1 COP a EUR
        (2, 1): 3800,       # 1 USD a COP
        (2, 2): 1,          # 1 USD a USD
        (2, 3): 0.88,       # 1 USD a EUR
        (3, 1): 4300,       # 1 EUR a COP
        (3, 2): 1.14,       # 1 EUR a USD
        (3, 3): 1           # 1 EUR a EUR
    }
    
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
            d_origen = int(input())  # La opción es 1-based
            
            # Elegir Monto
            monto = float(input("¿Cuánto dinero tiene? "))

            # Elegir divisa destino
            print("¿Qué divisa quiere?")
            print("   1. Pesos Colombianos")
            print("   2. Dólares")
            print("   3. Euros")
            d_salida = int(input())  # La opción es 1-based
            
            # Calcular conversión
            monto_convertido = convertir_divisa(monto, tasa_cambio[(d_origen, d_salida)])
            
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
