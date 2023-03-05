lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = [x + y for x, y in zip (lista_a, lista_b)]
print (list(zip(lista_a, lista_b)))

print (lista_soma)
#Zip é basicamente a uniao das duas listas



'''
lista_soma = []
    for i in range(len(lista_b)):
    lista_soma.append (lista_a [i] + lista_b [i])
print(lista_soma)'''
