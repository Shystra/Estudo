import pyautogui as py
import undetected_chromedriver as webdriver
import time
from selenium.webdriver.common.by import By
import random 

option = webdriver.ChromeOptions()
profile = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
option.add_argument (f"user-data-dir = {profile}")

driver = webdriver.Chrome (options = option, use_subprocess = True)

driver.get ('http://gmail.com.br/')
time.sleep(5)

py.click (x = 56, y = 189)
time.sleep (10)

py.write ('joao.lucas@interset.com.br')
time.sleep (5)

py.click ()
time.sleep (5)




py.position ()
print(py.position())









