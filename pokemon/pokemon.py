from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida

    @abstractmethod
    def atacar(self, contrincante):
        pass  # definir funcion para cada tipo

    tabla_de_tipos = {
        "agua": {"fuego": 0.5, "agua": 0.5, "planta": 2},
        "fuego": {"fuego": 0.5, "agua": 2, "planta": 0.5},
        "planta": {"fuego": 2, "agua": 0.5, "planta": 0.5},
    }

    def info(self):
        return f"====================\nNombre: {self.nombre}\nTipo: {self.tipo}\nVida: {self.vida}\n===================="


class Fuego(Pokemon):
    def atacar(self, contrincante):
        if contrincante.tipo in self.tabla_de_tipos[self.tipo]:
            efectividad = self.tabla_de_tipos[self.tipo][contrincante.tipo]
            contrincante.vida -= 10 * efectividad
            return (
                contrincante.vida,
                f"{self.nombre} atacó a {contrincante.nombre} con lanza llamas y le quitó {10 * efectividad} de vida",
            )


class Agua(Pokemon):  # Asegúrate de que "Pokemon" esté definido
    def atacar(self, contrincante):
        if contrincante.tipo in self.tabla_de_tipos[self.tipo]:
            efectividad = self.tabla_de_tipos[self.tipo][contrincante.tipo]
            danio = 10 * efectividad
            contrincante.vida -= danio
            return (
                contrincante.vida,
                f"{self.nombre} atacó a {contrincante.nombre} con hidrobomba y le quitó {danio} de vida",
            )


class Planta(Pokemon):
    def atacar(self, contrincante):
        if contrincante.tipo in self.tabla_de_tipos[self.tipo]:
            efectividad = self.tabla_de_tipos[self.tipo][contrincante.tipo]
            contrincante.vida -= 10 * efectividad
            return (
                contrincante.vida,
                f"{self.nombre} atacó a {contrincante.nombre} con hoja afilada y le quitó {10 * efectividad} de vida",
            )


if __name__ == "__main__":
    equipo = [
        Fuego("Charmander", "fuego", 100),
        Agua("Squirtle", "agua", 100),
        Planta("Bulbasaur", "planta", 100),
    ]

    for pokemon in equipo:
        print(pokemon.info())

    for i in range(equipo.__len__()):
        print(equipo[i].atacar(equipo[(i + 1) % 3]))
        print(equipo[i].atacar(equipo[(i + 2) % 3]))
        print(equipo[i].atacar(equipo[(i + 3) % 3]))
        print("")
