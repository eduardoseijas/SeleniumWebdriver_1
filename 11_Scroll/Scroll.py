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

driver.get("https://pixabay.com/es/images/search/?order=ec")
driver.maximize_window()
time.sleep(2)
#driver.execute_script("window.scrollTo(0,8000)")
#esta opcion anterior de scroll es una forma pero no la correcta

try:
    scroll1=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button--9NFL8 outline--rYKlp light--C3NP- stretch--PMRkR center--ZZf40']")))
    scroll1=driver.find_element(By.XPATH,"//a[@class='button--9NFL8 outline--rYKlp light--C3NP- stretch--PMRkR center--ZZf40']")
    ir=driver.execute_script("arguments[0].scrollIntoView;", scroll1)
    time.sleep(3)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

time.sleep(4)
driver.close()