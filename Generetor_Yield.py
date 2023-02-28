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

def gen1 ():
    p  ('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    p  ('ACABOU GEN1')


def gen3():
    p ('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    p ('ACABOU GEN3')


def gen2(gen=None):
    p ('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    p ('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    p (numero)
p ()
for numero in g2:
    p (numero)
p ()
for numero in g3:
    p (numero)
p ()


