import pprint

def p(v):
    pprint.pprint (v, sort_dicts = False, width = 40)

a = 18
b = 0


try:
    x = int (input("Digite um numero: ")
             )
except ValueError:
    print ("Entre com um numero valido."
             )
    

while True:
    try: 
        x = int(input('Digite um numero:  '))
        break
    except ValueError:
        print ("Entre com um numero valido. ")