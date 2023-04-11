def dividir (x, y):
    try:
        resultado = x / y
        print ("A resposta é :", resultado)
    except ZeroDivisionError:
        print("Divisao por zero")

dividir (3, 0)
dividir (3, 2)