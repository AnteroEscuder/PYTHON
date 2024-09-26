# Clase Animal
class Animal:
    def hablar(self):
        print("El animal hace un sonido")

# Clase derivada Perro que hereda de Animal
class Perro(Animal):  #Pongo entre paréntesis la clase de la que hereda , en este caso es Animal!
    def hablar(self):
        print("El perro dice: GUAU")

# Clase derivada Gato que hereda de Animal
class Gato(Animal):
    def hablar(self):
        print("El gato dice: MIAU")

# Creo objetos de las clases derivadas de Animal
mi_perro = Perro()
mi_gato = Gato()

# Llamo al método hablar en cada objeto
mi_perro.hablar() 
mi_gato.hablar()  
