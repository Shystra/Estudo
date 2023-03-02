def paramentros_decorador (nome):
    def decorador (fun):
        print('Decorador>', nome)

        def nova_funcao (*args, **kwargs):
            resultado = fun (*args, **kwargs)
            final = f'{resultado} {nome}'
            return final
        return nova_funcao
    return decorador    
@paramentros_decorador (nome = 'Segundo')       
@paramentros_decorador (nome = 'Primeiro')
def soma (x, y):
    return x + y

somando = soma (10, 5)
print (somando) 
