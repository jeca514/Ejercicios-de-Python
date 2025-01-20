class Paciente:
    def __init__(self,nombre):
        self._nombre = nombre
        self._edad = "Nan"
        self._hemoglobina = 0
        
        
    rangos_hemoglobina = {
    "0 - 1 mes": {"min": 13.0, "max": 26.0},
    "1 y <= 6 meses": {"min": 10.0, "max": 18.0},
    "6 y <= 12 meses": {"min": 11.0, "max": 15.0},
    "1 y <= 5 años": {"min": 11.5, "max": 16.0},
    "5 y <= 10 años": {"min": 12.6, "max": 15.5},
    "10 y <= 15 años": {"min": 13.0, "max": 15.5},
    "mujeres > 15 años": {"min": 12.0, "max": 16.0},
    "hombres > 15 años": {"min": 14.0, "max": 18.0}
    }

    @property
    def edad(self):
        return self._edad
    
    
    def seleccionar_edad(self):
        while True:
            try: 
                print("Elija su rango de edad: ")
                for i, rango in enumerate(self.rangos_hemoglobina.keys(), 1):
                    print(f"{i}. {rango}")
                opcion = int(input("Seleccione una opción (1-8): "))
                if 1 <= opcion <= len(self.rangos_hemoglobina):
                    self._edad = list(self.rangos_hemoglobina.keys())[opcion - 1]
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Intente de nuevo.")
        
if __name__ == "__main__":
    pasiente = Paciente("maria alejandra perez")
    pasiente.seleccionar_edad()
    print(f"edad: {pasiente.edad3}")