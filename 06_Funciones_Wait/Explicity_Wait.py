import time
from datetime import timezone
from os import times

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#Son necesarias estas 2 librerias para el explicity_wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()

driver.get("https://dfkaye.com/demos/alert-dialog-generator/")
driver.maximize_window()
btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']")))
time.sleep(2)
btn.click() #Al hacerla funcion arriba la puedo usar para hacerle click en esta parte
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Alert-Dialog']").click()
time.sleep(2)
driver.close()