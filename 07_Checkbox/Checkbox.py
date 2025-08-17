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

driver.get("https://www.ironspider.ca/forms/checkradio.htm")
driver.implicitly_wait(10)
driver.maximize_window()
btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='red']")))
time.sleep(2)
btn1.click()
btn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='yellow']")))
time.sleep(2)
btn2.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)
driver.close()