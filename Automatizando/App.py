import pyautogui as py
import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# arquivo = open ('cadastro.txt', 'r')

option = webdriver.ChromeOptions()
profile = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
option.add_argument (f"user-data-dir = {profile}")



driver = webdriver.Chrome (options = option, use_subprocess = True)

driver.get ('https://intersept.scond.com.br/#/home')
time.sleep(2)


driver.find_element(By.CLASS_NAME , "btn-block").click()
time.sleep (1)
print("LOGADO")

driver.find_element (By.CLASS_NAME , "form-control").click()
time.sleep (1)
print("CLICK")


    # ESCREVER

'''lista = [
'ALFREDO ANDERSEN',
'CANADÁ',
'CENTRAL PLACE',
'EDIFICIO FORTALEZA',
'GREENWOOD',
'INFINITE RESIDENCE',
'LAKEWOOD',
'LUXEMBOURG',
'ORIENTE WORK PLACE',
'RESIDENCE WINDSOR',
'RESIDENCIAL DO PARQUE',
'SOCIAL RESIDENCE',
'TIROL SANTA BÁRBARA',
'VILLE QUEBEC',
]

lista_recebe = []

for escreve in lista:
    pergunta = input ("Pesquisar qual cond? ")
    recebe_variavel = [lista_recebe]
'''

driver.find_element (By.CLASS_NAME , "form-control").send_keys(input('Escreva qual cond: '))
time.sleep (1)
print("CLICK ")

    
time.sleep (1)
driver.find_element (By.CLASS_NAME , "btn-pri1").click ()  
time.sleep (1)
print("PESQUISA")

driver.find_element (By.CLASS_NAME , 'icon-login').click ()
time.sleep (1)
print('DENTRO DO COND.!!!')

'''driver.find_element (By.CLASS_NAME , 'navbar-toggle').click()
time.sleep (3)
print('Ta quase la')'''

driver.find_elements (By.CLASS_NAME, 'centericon')[3].click()
time.sleep (2)
print('OK')

driver.find_element (By.CLASS_NAME, 'btn-primary').click()
time.sleep (2)
print('FORMULARIO')


## FORMULARIO ##

TIME_WAIT = 5

search_input_name = WebDriverWait (driver, TIME_WAIT).until(
    EC.presence_of_element_located (
    (By.NAME, 'texto')
    )
)

search_input_name.send_keys (input('NOME DO MALUCO(@): '))
time.sleep (3)

driver.find_elements (By.CLASS_NAME, 'ng-pristine')[5].send_keys(input('FALA O SOBRENOME AI CARALHO: '))
time.sleep (2)


#driver.find_elements (By.CLASS_NAME, 'ng-pristine')[10].click()
#time.sleep (2)

driver.find_elements (By.CLASS_NAME, 'ng-pristine')[9].send_keys (input('CPF PO: '))
time.sleep (2)
#CPF


driver.find_elements (By.CLASS_NAME, 'ng-pristine')[21].send_keys (input('CELULAR (QUASE ACABANDO CARALHO!!!): '))
time.sleep (2)


driver.find_element (By.ID, 'email').send_keys (input('COLOCA O E-MAIL AI PO: '))
time.sleep (2)

driver.find_elements (By.CLASS_NAME, 'form-control')[10].click()
time.sleep (2)

driver.find_elements (By.CLASS_NAME, 'dropdown-item')[24].click()
time.sleep (2)

driver.find_element (By.CLASS_NAME, 'btn-raised').click()
time.sleep (2)
print('Cadastrado!!!')







'''except (SyntaxError):
    print("Erro: " + SyntaxError)'''


        
