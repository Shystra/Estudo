from itertools import combinations, permutations, product

def print_inter (interator):
    print (*list (interator), sep = '\n')
    print()


pessoa = [
    'Joao', 'Joana', 'Luiz', 'Leticia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    [' masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

# print_inter (combinations (pessoa, 2))
# print_inter (permutations (pessoa, 2))

print_inter (product (*camisetas))


