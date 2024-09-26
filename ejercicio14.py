# Definición de la clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    # Método para depositar dinero en la cuenta
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    # Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:     # La cantidad tiene que ser mayor que 0 pero MENOR que el saldo para que pueda retirar ese dinero
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes o cantidad no válida.")

    # Método para mostrar la información de la cuenta
    def mostrar_informacion(self):
        print(f"Titular: {self.titular}, Saldo: {self.saldo}")

# Creación de un objeto de la clase CuentaBancaria
cuenta1 = CuentaBancaria("Antero", 500)

# Hago las operaciones 
cuenta1.mostrar_informacion()
cuenta1.depositar(200)     
cuenta1.retirar(100)       
cuenta1.retirar(700)     # En este último retiro de dinero me daría fondos insuficienetes puesto que sería mi saldo de la cuenta menor que 0
