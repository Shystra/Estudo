'''def fora (x):
    a = x

    def dentro ():
        return a
    return dentro

dentro1 = fora (10)

print (dentro1())'''

# Podemos também utilizar da seguinte forma.

def concatenar (string_inicial):
    valor_final = string_inicial

    def interna (valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar ('Teste 1 ')
print(*c ('Teste 2'), sep= '\n')

# nonlocal basicamente faz o python "lembrar" que a variavel existe

