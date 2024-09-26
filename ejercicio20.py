class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario_anual(self):
        return self.salario * 12

    def __str__(self):
        return f"Empleado: {self.nombre}, Salario Mensual: {self.salario}, Salario Anual: {self.calcular_salario_anual()}"

class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono

    def calcular_salario_anual(self):
        # El salario anual incluye el bono
        return (self.salario * 12) + self.bono

    def __str__(self):
        return f"Gerente: {self.nombre}, Salario Mensual: {self.salario}, Bono: {self.bono}, Salario Anual: {self.calcular_salario_anual()}"

class Programador(Empleado):
    def __init__(self, nombre, salario, lenguajes):
        super().__init__(nombre, salario)
        self.lenguajes = lenguajes  # Lista de lenguajes de programación

    def __str__(self):
        return f"Programador: {self.nombre}, Salario Mensual: {self.salario}, Lenguajes: {', '.join(self.lenguajes)}, Salario Anual: {self.calcular_salario_anual()}"

# Ejemplo de uso
if __name__ == "__main__":
    empleado1 = Empleado("Juan Pérez", 3000)
    gerente1 = Gerente("Ana Gómez", 5000, 2000)
    programador1 = Programador("Luis Sánchez", 4000, ["Python", "Java", "C++"])

    print(empleado1)
    print(gerente1)
    print(programador1)
