import time
from datetime import timezone
from os import times

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#Son necesarias estas 2 librerias para el explicity_wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#para que funcione el Select
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()

driver.get("https://testpages.eviltester.com/styled/basic-html-form-test.html")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

#se crea una variable con el driver.findelement, se selecciona el elemento
#se coloca quna nueva variable y dices que ella va a ser =Select(variable anterior)

sede=driver.find_element(By.XPATH,"//select[@name='dropdown']")
ds=Select(sede)
ds.select_by_visible_text("Drop Down Item 4")

time.sleep(2)

sede2=driver.find_element(By.XPATH,"//select[@name='dropdown']")
ds=Select(sede2)
ds.select_by_index(0)
time.sleep(2)

sede3=driver.find_element(By.XPATH,"//select[@name='dropdown']")
ds=Select(sede3)
ds.select_by_value("dd6")

time.sleep(2)
driver.close()