def verificar_par_impar(n):
    if n % 2 == 0:
        return f"{n} es un número par"
    else:
        return f"{n} es un número impar"


numero = 7
print(verificar_par_impar(numero))
