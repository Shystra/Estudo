'''import webbrowser as wb

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service = servico)

navegador.get ('https://github.com/Shystra')



def main ():
    while True:
        print('GitHub [1] or Sair [2]')
        x = int(input('>>>'))

        if x == 1:
            wb.open ('https://github.com/Shystra')      
        elif x == 2:
            input ('Aperte enter para sair...')
            break
main ()

'''

#https://gestao.pontotel.com.br/#/deviceManage/list

import undetected_chromedriver as webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Processo de Manipular o navegador e Gerar Relatorio
option = webdriver.ChromeOptions()
#profile = "C:\\Users\\localuser\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
profile = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
option.add_argument(f"user-data-dir={profile}")
#option.headless = True
driver = webdriver.Chrome(options=option,use_subprocess=True)
driver.get("https://bateponto.pontotel.com.br/#/")
WebDriverWait(driver, 900).until(EC.presence_of_element_located((By.ID , 'CMD_EXPORTARXLS'))).click()

time.sleep(2)


elemento = driver.find_element ('xpath',)