pessoa = {
    'nome': 'luiz',
    'sobrenome': 'mirante',
    'idade': 20,

 
    'endereço': [

    {'rua': 'tal tal', 'numero': 123}
    
    ]
}

print(pessoa['nome'])

print()

#podemos usar o for para trazer a chave inteira
for chave in pessoa:
    print(chave, pessoa[chave])
