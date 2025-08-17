import time
from datetime import timezone
from os import times
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
#Son necesarias estas 2 librerias para el explicity_wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#para que funcione el Select
from selenium.webdriver.support.ui import Select
#Esta es para el TimeoutException
from selenium.common.exceptions import TimeoutException
driver=webdriver.Chrome()

t=2

driver.get("https://testpages.eviltester.com/styled/alerts/fake-alert-test.html")
driver.maximize_window()
driver.find_element(By.ID,"fakealert").click()
time.sleep(t)
'''
driver.find_element(By.XPATH,"//button[@id='dialog-ok']").click()
time.sleep(t)
'''
#Version con try cash
try:
    buscar=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='dialog-ok']")))
    buscar.find_element(By.XPATH,"//button[@id='dialog-ok']").click()

except TimeoutException as ex:
    print(ex.msg)
    print("No encontro el elemento")
time.sleep(t)
driver.close()