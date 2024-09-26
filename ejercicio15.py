# Definición de la clase Coche
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método para mostrar la información del coche
    def mostrar_informacion(self):
        print(f"Coche: Marca = {self.marca}, Modelo = {self.modelo}")

# Creación de un objeto de la clase Coche
coche1 = Coche("Toyota", "Corolla")

# Llamar al método para  mostrar la información del coche
coche1.mostrar_informacion()
