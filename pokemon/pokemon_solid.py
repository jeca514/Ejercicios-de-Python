from abc import ABC, abstractmethod


class Pokemon(ABC):
    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida

    @abstractmethod
    def atacar(self, contrincante):
        pass  # definir función para cada tipo

    def info(self):
        return f"====================\nNombre: {self.nombre}\nTipo: {self.tipo}\nVida: {self.vida}\n===================="


class Fuego(Pokemon):
    def atacar(self, contrincante):
        efectividad = Efectividad.calcular_efectividad(self.tipo, contrincante.tipo)
        daño = 10 * efectividad
        contrincante.vida -= daño
        return (
            contrincante.vida,
            f"{self.nombre} atacó a {contrincante.nombre} con lanza llamas y le quitó {daño} de vida",
        )


class Agua(Pokemon):
    def atacar(self, contrincante):
        efectividad = Efectividad.calcular_efectividad(self.tipo, contrincante.tipo)
        daño = 10 * efectividad
        contrincante.vida -= daño
        return (
            contrincante.vida,
            f"{self.nombre} atacó a {contrincante.nombre} con hidrobomba y le quitó {daño} de vida",
        )


class Planta(Pokemon):
    def atacar(self, contrincante):
        efectividad = Efectividad.calcular_efectividad(self.tipo, contrincante.tipo)
        daño = 10 * efectividad
        contrincante.vida -= daño
        return (
            contrincante.vida,
            f"{self.nombre} atacó a {contrincante.nombre} con hoja afilada y le quitó {daño} de vida",
        )


class Efectividad:
    tabla_de_tipos = {
        "agua": {"fuego": 0.5, "agua": 0.5, "planta": 2},
        "fuego": {"fuego": 0.5, "agua": 2, "planta": 0.5},
        "planta": {"fuego": 2, "agua": 0.5, "planta": 0.5},
    }

    @staticmethod
    def calcular_efectividad(atacante, contrincante):
        return Efectividad.tabla_de_tipos.get(atacante, {}).get(contrincante, 1)


if __name__ == "__main__":
    equipo = [
        Fuego("Charmander", "fuego", 100),
        Agua("Squirtle", "agua", 100),
        Planta("Bulbasaur", "planta", 100),
    ]

    for pokemon in equipo:
        print(pokemon.info())

    for i in range(len(equipo)):
        print(equipo[i].atacar(equipo[(i + 1) % len(equipo)]))
        print(equipo[i].atacar(equipo[(i + 2) % len(equipo)]))
        print(equipo[i].atacar(equipo[(i + 3) % len(equipo)]))
        print("")

q- 