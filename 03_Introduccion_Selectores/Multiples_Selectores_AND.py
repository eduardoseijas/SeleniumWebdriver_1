import time
from os import times

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"userName").send_keys("Eduardo")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys("eduardoseijas@hotmail.com")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"#currentAddress").send_keys("Dirección 1")
time.sleep(2)
driver.find_element(By.ID,"permanentAddress").send_keys("Dirección 2")
time.sleep(2)
driver.execute_script("window.scrollTo(0,300)") #esta funciona para hacer un scroll y bajar o subir la pag
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#submit").click()
time.sleep(3)
driver.close()



