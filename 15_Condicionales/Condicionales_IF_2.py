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

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)
bt1=driver.find_element(By.XPATH,"//body/div[@id='fixedban']/div/div[1]")
print(bt1.is_enabled())

if (bt1.is_enabled()==True):
    print("Puedes dar click")
    driver.execute_script("window.scrollTo(0,300)")
    bt1.click()
    time.sleep(3)
else:
    print("No puedes dar click")

driver.close()