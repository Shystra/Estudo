def ehPar (n):
    r = (n % 2==0)
    return r

def soma_par (lst):
    soma = 0 # Variavel acumuladora
    for num in lst: # Para cara numero na lst
        if (ehPar(num)): # Se o numero da lista for par retorna a soma + num
            soma = soma + num
        return soma     
    
lista = [10, 2, 5, 7, 6, 3]
soma = soma_par (lista)
print (f'O somatorio dos elementos pares da lista é: {soma}')


def testpar (n):
    r = (n % 2 ==0)
    return r

def somatest (lista):
    soma = 0
    for num in lista:
        if (testpar(num)): #Se for par
            soma = num + soma
        return soma 
        
lista_exemplo = [10, 20, 50, 5]
soma = somatest (lista_exemplo)
print (soma)