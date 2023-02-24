import pprint

def p(v):
    pprint.pprint (v, sort_dicts = False, width = 40)

'''def generator (n = 0, maximium = 10):
    while True:
        yield n 
        n += 1

        if n >= maximium:
            return

gen = generator (n = 5)
for n in gen:
    p(n)'''

def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()


