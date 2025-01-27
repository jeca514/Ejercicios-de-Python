# **EJERCICIO**

Crear un programa que simule ataques de diferentes tipos de Pokémon usando polimorfismo, donde cada Pokémon tenga un ataque único.

**1. Crear una clase base llamada Pokemon:**

- 1.1. Define un método llamado atacar en la clase base.
  - Este método no debe tener implementación (puedes usar raise NotImplementedError).
  - Servirá como "plantilla" para las subclases que lo sobrescribirán.
- 1.2. Incluye un mensaje opcional dentro del método atacar, como: "Este método debe ser implementado por las subclases".

**2. Crear clases derivadas para los tipos de Pokémon:**

- 2.1. Define al menos tres clases que hereden de la clase Pokemon.

- 2.2. Crea las siguientes clases de ejemplo:
  - Charmander (tipo Fuego).
  - Squirtle (tipo Agua).
  - Bulbasaur (tipo Planta).

- 2.3. En cada subclase, sobrescribe el método atacar para que realice lo siguiente:
  - Imprima un mensaje único que indique el nombre del Pokémon y su ataque característico.

**3. Crear un equipo de Pokémon:**

- 3.1. Genera una lista llamada pokemon_equipo, que contenga instancias de las clases creadas:
  - Una instancia de Charmander.
  - Una instancia de Squirtle.
  - Una instancia de Bulbasaur.

**4. Simular la batalla:**

- 4.1. Itera sobre la lista pokemon_equipo usando un bucle (for).
- 4.2. Llama al método atacar de cada Pokémon dentro del bucle.
- 4.3. Asegúrate de que el ataque correcto se imprima según el tipo de Pokémon.
