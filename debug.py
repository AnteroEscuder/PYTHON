def sumar(a, b, iterations):
    results = []
    for i in range(iterations):
        results.append(a + b)
    return results

def restar(a, b, iterations):
    results = []
    for i in range(iterations):
        results.append(a - b)
    return results

def multiplicar(a, b, iterations):
    results = []
    for i in range(iterations):
        results.append(a * b)
    return results

def dividir(a, b, iterations):
    results = []
    for i in range(iterations):
        if b == 0:
            results.append("Error: División por cero")
        else:
            results.append(a / b)
    return results

# Test functions
resultado = sumar(2,2,2)
print("Resultado sumar: " + str(resultado))

resultados = restar(2,3,3)
print(f"Resultado restar: {resultado}")

resultado = multiplicar(2,3,2)
print(f"Resultado multiplicar: {resultado}")

resultado = dividir(2,2,2)
print(f"Resultado dividir: {resultado}")
