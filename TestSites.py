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

