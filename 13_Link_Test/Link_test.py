import time
from datetime import timezone
from os import times
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#Son necesarias estas 2 librerias para el explicity_wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#para que funcione el Select
from selenium.webdriver.support.ui import Select
#Esta es para el TimeoutException
from selenium.common.exceptions import TimeoutException
driver=webdriver.Chrome()

t=1

driver.get("https://testpages.eviltester.com/styled/index.html")
driver.maximize_window()
time.sleep(t)

#Obtener todos los links de la pagina

links=driver.find_elements(By.TAG_NAME,"a")
print("El numero de links que hay en la pag es: ", len(links))

for num in links:
    print(num.text)

driver.find_element(By.LINK_TEXT,"HTML Form Example").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT,"Index").click()
time.sleep(t)