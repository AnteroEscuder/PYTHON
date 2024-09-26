
class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    # Método para el área
    def calcular_area(self):
        return self.ancho * self.altura

    # Método para  el perímetro
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.altura)

# Creación de un objeto de la clase Rectangulo
rectangulo1 = Rectangulo(5, 10)

# Saco el área y el perímetro del rectángulo
print(f"Área del rectángulo: {rectangulo1.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo1.calcular_perimetro()}")
