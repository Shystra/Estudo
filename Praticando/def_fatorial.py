def fatorial_interativo (n):
    fatorial = 1
    for i in range (1, n + 1):
        fatorial = fatorial * i
    return fatorial

numero = 5
print (f'O fatorial de {numero} é: {fatorial_interativo(numero)}')