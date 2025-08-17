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

driver.get("https://testpages.eviltester.com/styled/basic-html-form-test.html")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollTo(0,900)")

#Dentro del Try: el XPATH correcto es //select[@name='dropdown'], le agregue un 1 //select[@name='dropdown1']
#para que diera error, pudiera continuar y generara el mensaje de error
#Parte de la prueba para que funcionara try catch

try:
    select1=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='dropdown1']")))
    item=Select(select1)
    item.select_by_visible_text("Drop Down Item 2")
    time.sleep(2)
    item.select_by_index(4)
    time.sleep(2)
    item.select_by_value("dd6")
    time.sleep(2)
except TimeoutException as ex:
    print(ex.msg)
    print("El bloque 1 fallo, pudo continuar e hizo el 2do bloque")

#Segundo Bloque

dropdow=Select(driver.find_element(By.XPATH,"//select[@name='multipleselect[]']"))
dropdow.select_by_index(1)
time.sleep(1)

dropdow.deselect_by_index(3)
time.sleep(1)

dropdow.select_by_visible_text("Selection Item 1")
time.sleep(1)

dropdow.select_by_value("ms3")
time.sleep(1)

driver.close()