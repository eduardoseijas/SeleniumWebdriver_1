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
#Conditionales
#if

driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(t)
titulo=driver.find_element(By.XPATH,"//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())
time.sleep(t)
bt1=driver.find_element(By.XPATH,"//div[@class='category-cards']//div[1]//div[1]//div[1]")
if(titulo.is_displayed()==True):
    print("Existe la imagen")
    bt1.click()
    time.sleep(2)
else:
    print("No existe la imagen")
driver.close()