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

t=1

driver.get("https://testpages.eviltester.com/styled/basic-html-form-test.html")
driver.maximize_window()
time.sleep(t)

driver.find_element(By.XPATH,"//input[@name='username']").send_keys("EduardoSeijas@hotmail.com" + Keys.TAB + "eds12390")
time.sleep(t)
driver.find_element(By.XPATH,"//textarea[@name='comments']").clear()
time.sleep(t)
driver.find_element(By.XPATH,"//textarea[@name='comments']").send_keys("Este comentario es del reto 1, practicando automatizar una llena de formulario")
time.sleep(t)
imagen=driver.find_element(By.XPATH,"//input[@name='filename']")
time.sleep(t)
imagen.send_keys("C://Practica_Selenium_2//10_Upload_file//Imagenes")
#saco la ruta desde explore en C:\Practica_Selenium_2\10_Upload_file\Imagenes y le invierto \ por //
time.sleep(t)
driver.find_element(By.XPATH,"//input[@value='cb3']").click()
time.sleep(t)
driver.find_element(By.XPATH,"//input[@value='cb1']").click()
time.sleep(t)
driver.find_element(By.XPATH,"//input[@value='rd1']").click()
time.sleep(t)
#Scroll
driver.execute_script("window.scrollTo(0,4000)")
#Select
sele1=Select(driver.find_element(By.CSS_SELECTOR,"select[name='multipleselect[]']"))
sele1.deselect_by_index(3)
time.sleep(t)
sele2=Select(driver.find_element(By.CSS_SELECTOR,"select[name='multipleselect[]']"))
sele2.select_by_visible_text("Selection Item 1")
time.sleep(t)
sele3=Select(driver.find_element(By.XPATH,"//select[@name='multipleselect[]']"))
sele3.select_by_value("ms3")
time.sleep(t)

#Dropdow

dropdown1=Select(driver.find_element(By.XPATH,"//select[@name='dropdown']"))
dropdown1.select_by_visible_text("Drop Down Item 5")
time.sleep(t)
#Sumit
driver.find_element(By.XPATH,"//input[@value='submit']").click()
time.sleep(t)
#Scroll
driver.execute_script("window.scrollTo(0,2000)")
time.sleep(t)
driver.close()
