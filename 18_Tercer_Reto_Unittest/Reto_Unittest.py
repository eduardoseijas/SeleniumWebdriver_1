import time
import unittest
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

#Al crear la class con el self.driver = webdriver.Chrome()
#No se debe colocar arriba junto con las librerias driver=webdriver.Chrome() porque te despliega una ventana vacia


class PruebaLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        t=2


    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        user=driver.find_element(By.XPATH,"//input[@id='user-name']")
        pas=driver.find_element(By.XPATH,"//input[@id='password']")
        btn1=driver.find_element(By.XPATH,"//input[@id='login-button']")
        time.sleep(2)
        user.send_keys("Eduardo")
        pas.send_keys("admin123")
        btn1.click()
        error=driver.find_element(By.XPATH,"//h3[@data-test='error']")
        error=error.text
        #print(error)
        if (error=="Epic sadface: Username and password do not match any user in this service"):
            print("El error es correctos")
            print("Los datos no son correctos")
            print("Prueba 1")
        time.sleep(2)

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        user = driver.find_element(By.XPATH, "//input[@id='user-name']")
        pas = driver.find_element(By.XPATH, "//input[@id='password']")
        btn1 = driver.find_element(By.XPATH, "//input[@id='login-button']")
        time.sleep(2)
        user.send_keys()
        pas.send_keys("admin123")
        btn1.click()
        error = driver.find_element(By.XPATH, "//h3[normalize-space()='Epic sadface: Username is required']")
        error = error.text
        # print(error)
        if (error == "Epic sadface: Username is required"):
            print("El error es correctos")
            print("Falta agregar el usuario")
            print("Prueba 2")
        time.sleep(2)

    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        user = driver.find_element(By.XPATH, "//input[@id='user-name']")
        pas = driver.find_element(By.XPATH, "//input[@id='password']")
        btn1 = driver.find_element(By.XPATH, "//input[@id='login-button']")
        time.sleep(2)
        user.send_keys("Eduardo")
        pas.send_keys()
        btn1.click()
        error = driver.find_element(By.XPATH, "//div[@class='error-message-container error']")
        error = error.text
        # print(error)
        if (error == "Epic sadface: Password is required"):
            print("El error es correctos")
            print("Falta agregar el password")
            print("Prueba 3")
        time.sleep(2)

    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        user = driver.find_element(By.XPATH, "//input[@id='user-name']")
        pas = driver.find_element(By.XPATH, "//input[@id='password']")
        btn1 = driver.find_element(By.XPATH, "//input[@id='login-button']")
        time.sleep(2)
        user.send_keys()
        pas.send_keys()
        btn1.click()
        error = driver.find_element(By.XPATH, "//h3[normalize-space()='Epic sadface: Username is required']")
        error = error.text
        # print(error)
        if (error == "Epic sadface: Username is required"):
            print("El error es correctos")
            print("Falta agregar usuario y contraseña")
            print("Prueba 4")
        time.sleep(2)


    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        user = driver.find_element(By.XPATH, "//input[@id='user-name']")
        pas = driver.find_element(By.XPATH, "//input[@id='password']")
        btn1 = driver.find_element(By.XPATH, "//input[@id='login-button']")
        time.sleep(2)
        user.send_keys("visual_user")
        pas.send_keys("secret_sauce")
        btn1.click()
        time.sleep(2)
        logo=driver.find_element(By.XPATH,"//div[@class='app_logo']")
        logo=logo.text
        if(logo=="Swag Labs"):
            print("El usuario a ingresado Correctamente")
            print("Prueba 5")
        else:
            print("No has ingresado al sistema")
            print("Prueba 5")

    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__=='__main__':
    unittest.main()