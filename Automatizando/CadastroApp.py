import pyautogui as py
import time
from selenium.webdriver.common.by import By


#time.sleep(4)

py.click (x = 2367, y = 327) # NOME
time.sleep (3)
py.write ('TESTE1')
time.sleep (2)
print ('Ok')


py.click (x = 3012, y = 323) # SOBRENOME
time.sleep (3)
py.write ('TESTE2')
time.sleep (2)
print ('Ok')


py.click (x = 3036, y = 416) # CPF
time.sleep (3)
py.write ('06384159937')
time.sleep (2)
print ('Ok')

py.click (x = 3355, y = 470) # TELEFONE
time.sleep (3)
py.write ('41988806319')
time.sleep (2)
print ('Ok')

py.click (x = 3630, y = 489) # CELULAR
time.sleep (3)
py.write ('41988806319')
time.sleep (2)
print ('Ok')


py.click (x = 2596, y = 560) # E-MAIL
time.sleep (3)
py.write ('TESTE6')
time.sleep (2)
print ('Ok')

py.click (x = 2988, y = 557) # GRUPOS
time.sleep (3)
print('Ok')


py.click (x = 2964, y = 714) # MORADOR
time.sleep (3)
print ('Ok')


time.sleep (3)
# print ('Ok')

py.click () 
print(py.position())