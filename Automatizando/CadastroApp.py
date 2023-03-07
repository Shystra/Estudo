import pyautogui as py
import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as webdriver
import time


option = webdriver.ChromeOptions()
profile = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
option.add_argument (f"user-data-dir = {profile}")



driver = webdriver.Chrome (options = option, use_subprocess = True)

driver.get ('https://intersept.scond.com.br/#/home')
time.sleep(5)


try:
    driver.find_element(By.CLASS_NAME , "btn-block").click()
    time.sleep (5)
    print("Logado")

    driver.find_element (By.CLASS_NAME , "form-control").click()
    time.sleep (5)
    print("Click ")

    # ESCREVER
    py.write ('comando.txt')
    time.sleep(5)
    print("Digitou")

    driver.find_element (By.CLASS_NAME , "btn-pri1").click ()  
    time.sleep (5)
    print("Pesquisa")
 
except(SyntaxError):
    print("Erro: " + SyntaxError)


'''for cond in matriculas:
    pergunta = input('Gostaria de continuar''?')
    if pergunta == 'Sim':
        driver.find_element(By.ID , 'senhanumerica').send_keys (mat)
        time.sleep (2)'''
        




'''
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
print(py.position()) '''