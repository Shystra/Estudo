from itertools import zip_longest

l1 = ['Salvador' , 'Ubatuba' , 'Belo Horizonte']
l2 = ['BA' , 'SP' , 'RJ', 'MG']

print(list(zip (l1, l2))) 
print()
print(list(zip_longest (l1, l2, fillvalue = 'SEM CIDADE'))) # Usa a lista maior
