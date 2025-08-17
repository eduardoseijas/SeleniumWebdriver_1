import time
from os import times

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#para navegar de una ruta web a otra

driver=webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)
driver.get("https://jupyter.org/install")
time.sleep(2)
driver.get("https://chromewebstore.google.com/detail/css-and-xpath-checker/aoinfihhckpkkcpholfhmkeplbhddipe?hl=Es")
time.sleep(2)

#Con la funcion back() te permite regresar a la web anterior

driver.execute_script("window.history.go(-1)")
time.sleep(2)
driver.execute_script("window.history.go(-1)")
time.sleep(3)

driver.execute_script("window.history.go(2)")
time.sleep(3)
driver.close()

#Tambien esta la opcion driver.forward(), pero si es mas de 2 segundos puede dar error
#Este es para ir a la siguiente pag web hacia adelante