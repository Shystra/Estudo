def decoradora (fun):
    print ('Decoradora 1')

    def aninhada (*args, **kwargs):
        print ("Teste Aninhada")
        resultado = fun (*args, **kwargs)
        return resultado + 30
    return aninhada





@decoradora 
def soma (x, y):
    return x + y

exemplo_aninhada = soma (10, 5)
print (exemplo_aninhada)

