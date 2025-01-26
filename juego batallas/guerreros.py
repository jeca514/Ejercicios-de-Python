import random

class Guerrero:
    def __init__(self, faccion, clave_raza):  # Recibe facción y clave
        self._faccion = faccion
        
        # Obtiene la raza según la facción y clave
        if faccion == "benevola":
            self._raza = self.faccion_benevola.get(clave_raza)
        elif faccion == "malvada":
            self._raza = self.faccion_malvada.get(clave_raza)
        else:
            raise ValueError("Facción inválida")
        
        # Valida que la raza exista
        if self._raza is None:
            raise ValueError(f"Clave {clave_raza} no existe en la facción {faccion}")

    faccion_benevola = {
        1: "Ositos",
        2: "Principes",
        3: "Enanos",
        4: "Caris",
        5: "Fulos"
    }

    faccion_malvada = {
        1: "Lolos",
        2: "Fulanos",
        3: "Hoggis",
        4: "Lurcos",
        5: "Trollis"
    }

    victoria_benevola = {
        "Ositos": {"Lolos": 2, "Fulanos": 3, "Hoggis": 5, "Lurcos": 2, "Trollis": 1},
        "Principes": {"Lolos": 0.5, "Fulanos": 0.7, "Hoggis": 0.5, "Lurcos": 1, "Trollis": 0.3},
        "Enanos": {"Lolos": 0.3, "Fulanos": 0.5, "Hoggis": 1, "Lurcos": 0.3, "Trollis": 0.1},
        "Caris": {"Lolos": 2, "Fulanos": 1, "Hoggis": 5, "Lurcos": 2, "Trollis": 3},
        "Fulos": {"Lolos": 1, "Fulanos": 0.5, "Hoggis": 2, "Lurcos": 3, "Trollis": 0.7},
    }
    
    def generador
    
    def peso_victoria(self, enemigo):
        # if que determina facción 
        if self._faccion == "benevola":
            peso_victoria = self.victoria_benevola[self._raza][enemigo._raza]
            return peso_victoria
        else:
            peso_victoria = 1/self.victoria_benevola[enemigo._raza][self._raza]
            return peso_victoria
        
    
class Batallon:
    def __init__(self, faccion):
        self.faccion = faccion
        self.guerreros = []  # Lista de objetos Guerrero

    def agregar_guerrero(self, clave_raza):
        nuevo_guerrero = Guerrero(faccion=self.faccion, clave_raza=clave_raza)
        self.guerreros.append(nuevo_guerrero)

    def generar_aleatorio(self, cantidad):
        for _ in range(cantidad):
            clave_random = random.randint(1, 5)  # Asume 5 razas por facción
            self.agregar_guerrero(clave_random)

    def calcular_fuerza(self, enemigo):
         # if que determina facción 
        if self._faccion == "benevola":
            peso_victoria = self.victoria_benevola[self._raza][enemigo._raza]
            return peso_victoria
        else:
            peso_victoria = 1/self.victoria_benevola[enemigo._raza][self._raza]
            return peso_victoria
       
