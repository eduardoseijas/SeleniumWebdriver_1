from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://demoqa.com/")
print("Bienvenido a Selenium")
print(driver.title)
driver.close()



