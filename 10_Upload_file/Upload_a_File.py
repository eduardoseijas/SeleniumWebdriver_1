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

driver.get("https://testpages.eviltester.com/styled/file-upload-test.html")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(2)

try:
    buscar=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='fileinput']")))
    buscar=driver.find_element(By.XPATH,"//input[@id='fileinput']")
    buscar.send_keys("C://Practica_Selenium_2//10_Upload_file//Imagenes//demo1.jpg")
    #en la ruta hay que usar // no \
    driver.find_element(By.XPATH,"//input[@id='itsanimage']").click()
    driver.find_element(By.XPATH,"//input[@name='upload']").click()
    time.sleep(2)
except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")



time.sleep(2)
driver.close()