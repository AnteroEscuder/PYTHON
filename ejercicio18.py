# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método para mostrar la información del vehículo
    def informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# Clase derivada Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llama al constructor de la clase base
        self.puertas = puertas

    # Método específico de la clase Coche
    def informacion(self):
        super().informacion()  # Llama al método de la clase base
        print(f"Número de puertas: {self.puertas}")

# Clase derivada Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)  # Llama al constructor de la clase base
        self.tipo = tipo

    # Método específico de la clase Bicicleta
    def informacion(self):
        super().informacion()  # Llama al método de la clase base
        print(f"Tipo: {self.tipo}")

# Crear objetos de las clases derivadas
coche = Coche("Toyota", "Corolla", 4)
bicicleta = Bicicleta("Giant", "ATX", "Montañera")

# Mostrar la información de cada vehículo
print("Información del coche:")
coche.informacion()
print("\nInformación de la bicicleta:")
bicicleta.informacion()
