import undetected_chromedriver as webdriver
import time
from selenium.webdriver.common.by import By
import random

option = webdriver.ChromeOptions ()
profile = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
option.add_argument (f"user-data-dir = {profile}")

driver = webdriver.Chrome (options = option, use_subprocess = True)

driver.get ("https://www.youtube.com/")
time.sleep(5)