import time
from os import times

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(10) #esto permite que te de un plazo de segundos, para ubicar el objeto


nom=driver.find_element(By.XPATH,"//input[@id='userName']")
nom.send_keys("Eduardo")
time.sleep(2)
email=driver.find_element(By.XPATH,"//input[@id='userEmail']")
email.send_keys("eduardoseijas@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys("Dirección 1")
time.sleep(2)
driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']").send_keys("Dirección 2")
time.sleep(2)
driver.execute_script("window.scrollTo(0,300)") #esta funciona para hacer un scroll y bajar o subir la pag
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='submit']").click()
time.sleep(3)
driver.close()
