# Clase base InstrumentoMusical
class InstrumentoMusical:
    def tocar(self):
        print("El instrumento musical suena.")

# Clase derivada Piano que hereda de InstrumentoMusical
class Piano(InstrumentoMusical):
    def tocar(self):
        print("El piano suena: ")

# Clase derivada Guitarra que hereda de InstrumentoMusical
class Guitarra(InstrumentoMusical):
    def tocar(self):
        print("La guitarra suena: ")

# Crear objetos de las clases derivadas
piano = Piano()
guitarra = Guitarra()

# Llamar al método tocar en cada objeto
piano.tocar()    
guitarra.tocar()  
