def soma (x, y):
    return x + y

def multiplica (x, y):
    return x * y

def executa (funcao, x):
    def interna (y):
        return funcao (x, y)
    return interna

def executay (funcao, y):
    def internay (x):
        return funcao (x, y)
    return internay

soma1 = executa (soma, 5)
soma2 = executay (multiplica, 10)

print(soma1 (10))
print(soma2 (10)) 