# Clase base FiguraGeometrica
class FiguraGeometrica:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def area(self):
        raise NotImplementedError("Este método debe ser sobrescrito en clases derivadas.")   # Sirve para indicar que el metodo (en este caso area)solo funciona en clases derivadas, es decir que solo rectángulo y triángulo pueden usar este método porque son las clases deriavdas!!

# Clase derivada Rectangulo que hereda de FiguraGeometrica
class Rectangulo(FiguraGeometrica):
    def area(self):
        return self.ancho * self.altura

# Clase derivada Triangulo que hereda de FiguraGeometrica
class Triangulo(FiguraGeometrica):
    def area(self):
        return (self.ancho * self.altura) / 2

# Crear objetos de las clases derivadas
rectangulo = Rectangulo(5, 10)       # El constructor lo hereda de FiguraGeometrica!
triangulo = Triangulo(5, 10)         # El constructor lo hereda de FiguraGeometrica!

# Calculo y muestro el área de cada figura
print(f"Área del rectángulo: {rectangulo.area()}") 
print(f"Área del triángulo: {triangulo.area()}")    
