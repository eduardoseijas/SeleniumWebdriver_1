import time
from os import times

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#funcion para usar el tabulador Keys.TAB y Keys.enter
#para esta funcion se debe concatenar con el + si deseas escribir o llenar alguna info en la web

driver=webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)
nom=driver.find_element(By.XPATH,"//input[@id='userName']")
nom.send_keys("Eduardo")
time.sleep(2)
nom.send_keys(Keys.TAB + "eduardo18@gmail.com" + Keys.TAB + "Direccion 1" + Keys.TAB + "Direccion2" + Keys.TAB + Keys.ENTER)
time.sleep(2)
driver.execute_script("window.scrollTo(0,300)") #esta funciona para hacer un scroll y bajar o subir la pag
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#item-1").click()
time.sleep(2)
driver.close()
