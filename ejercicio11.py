
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Creación de un objeto de tipo Persona
persona1 = Persona("Juan", 30)

# Muestro los atributos del objeto persona1
persona1.mostrar_informacion()
