def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a


numero1 = 48
numero2 = 18

mcd = calcular_mcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es: {mcd}")
