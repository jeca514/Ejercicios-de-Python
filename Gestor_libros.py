# Decorador para registrar acciones
def registrar_accion(funcion_original):
    def nueva_funcion(*args, **kwargs):
        accion = f"Ejecutando '{funcion_original.__name__}' con args: {args[1:]} y kwargs: {kwargs}"
        print(f"Registrando acción: {accion}")  # Aquí se registra la acción
        with open("registro.txt", "a") as archivo:  # Guardar en archivo
            archivo.write(accion + "\n")
        return funcion_original(*args, **kwargs)  # Llama a la función original
    return nueva_funcion

# Clase con una función decorada
class Biblioteca:
    def __init__(self):
        self.libros = {}

    @registrar_accion
    def agregar_libro(self, titulo, autor):
        self.libros[titulo] = autor
        print(f"Libro '{titulo}' agregado con éxito.")

    @registrar_accion
    def eliminar_libro(self, titulo):
        if titulo in self.libros:
            del self.libros[titulo]
            print(f"Libro '{titulo}' eliminado con éxito.")
        else:
            print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

# Crear una instancia de la clase
biblioteca = Biblioteca()

# Experimentar con las funciones decoradas
biblioteca.agregar_libro("1984", "George Orwell")
biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez")
biblioteca.eliminar_libro("1984")
biblioteca.eliminar_libro("El Quijote")

# Verifica el archivo 'registro.txt' para ver los registros.
