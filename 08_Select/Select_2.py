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
driver.execute_script("window.scrollTo(0,900)")
time.sleep(2)

dropdow=Select(driver.find_element(By.XPATH,"//select[@name='multipleselect[]']"))
dropdow.select_by_index(1)
time.sleep(2)

dropdow.deselect_by_index(3)
time.sleep(2)

dropdow.select_by_visible_text("Selection Item 1")
time.sleep(2)

dropdow.select_by_value("ms3")
time.sleep(2)

driver.close()