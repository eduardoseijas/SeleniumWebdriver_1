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

#Con la funcion back() te permite regresar a la web anterior, si tarda mas de 3 o 4 segundos da error
#esta la opcion de hacerlo con una funcion de javascripts .execute_script("window.history.go(-1)")
#lo aplico en NavegarFuncionJava_execute_script

driver.back()
time.sleep(2)
driver.back()
time.sleep(2)
driver.close()