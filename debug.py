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
