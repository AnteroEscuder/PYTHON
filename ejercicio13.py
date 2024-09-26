# La clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    # Método para mostrar la información del estudiante
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Curso: {self.curso}")

# Creación de varios objetos de tipo Estudiante
estudiante1 = Estudiante("Antero", 20, "DWEC")
estudiante2 = Estudiante("Carlos", 22, "DWES")
estudiante3 = Estudiante("María", 19, "DESPLIEGUE")
estudiante4 = Estudiante("Luis", 21, "iNTERFACES")

#  Guardo los estudiantes en una lista
lista_estudiantes = [estudiante1, estudiante2, estudiante3, estudiante4]

# Hago un for each y saco la info de cada estudiante
for estudiante in lista_estudiantes:
    estudiante.mostrar_informacion()
