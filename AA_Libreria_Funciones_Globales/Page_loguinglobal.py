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
from AA_Libreria_Funciones_Globales.Libreria_Funciones import Libreria_Funciones_Globales
import pytest

class Page_Loguinglobal():

    def __init__(self,driver):
        self.driver=driver

    def Loguin_1(self,email,clave,mensaje,tiempo=.5):
        global driver
        driver = webdriver.Chrome()
        f=Libreria_Funciones_Globales(driver)
        f = Libreria_Funciones_Globales(driver)  # IMPORTANTE NUNCA OLVIDAR EN EL (), colocar (driver)
        f.Navegar("https://www.saucedemo.com/", 1)
        driver.maximize_window()
        f.Text_Mixto_Validado("xpath", "//input[@id='user-name']", email, 1)
        f.Text_Mixto_Validado("xpath", "//input[@id='password']", clave, 1)
        f.Click_Mixto("xpath", "//input[@id='login-button']", 1)
        e1 = f.SEX("//h3[@data-test='error']")
        e1 = e1.text
        # print("Epic sadface: Username and password do not match any user in this service")
        if (e1 == mensaje):
            print("Prueba de validacion exitosa, debes colocar la contraseña correcta")
        else:
            print("La prueba de validacion es incorrecta")
        time.sleep(tiempo)
        driver.close()

    def Loguin_2 (self,email,clave,mensaje,tiempo=.5):
        driver = webdriver.Chrome()
        f=Libreria_Funciones_Globales(driver) #IMPORTANTE NUNCA OLVIDAR EN EL (), colocar (driver)
        f.Navegar("https://www.saucedemo.com/",1)
        driver.maximize_window()
        f.Text_Mixto_Validado("xpath","//input[@id='user-name']",email,1)
        f.Text_Mixto_Validado("xpath","//input[@id='password']",clave,1)
        f.Click_Mixto("xpath","//input[@id='login-button']",1)
        e1=f.SEX("//h3[normalize-space()='Epic sadface: Username is required']")
        e1=e1.text
        #print("Epic sadface: Username and password do not match any user in this service")
        if (e1==mensaje):
            print("Prueba de validacion exitosa, debes colocar el correo de usuario")
        else:
            print("La prueba de validacion es incorrecta")

        time.sleep(tiempo)
        driver.close()

    def Loguin_3(self,email,clave,mensaje,tiempo=.5):
        global driver
        driver = webdriver.Chrome()
        f=Libreria_Funciones_Globales(driver) #IMPORTANTE NUNCA OLVIDAR EN EL (), colocar (driver)
        f.Navegar("https://www.saucedemo.com/",1)
        driver.maximize_window()
        f.Text_Mixto_Validado("xpath","//input[@id='user-name']",email,1)
        f.Text_Mixto_Validado("xpath","//input[@id='password']",clave,1)
        f.Click_Mixto("xpath","//input[@id='login-button']",1)
        e1=f.SEX("//h3[contains(text(),'Epic sadface: Username and password do not match a')]")
        e1=e1.text
        #print("Epic sadface: Username and password do not match any user in this service")
        if (e1==mensaje):
            print("Prueba de validacion exitosa, debes colocar correctamente el correo usuario")
        else:
            print("La prueba de validacion es incorrecta")

        time.sleep(tiempo)
        driver.close()

    def Loguin_4(self,email,clave,mensaje,tiempo=0.5):
        global driver
        driver = webdriver.Chrome()
        f = Libreria_Funciones_Globales(driver)  # IMPORTANTE NUNCA OLVIDAR EN EL (), colocar (driver)
        f.Navegar("https://www.saucedemo.com/", 1)
        driver.maximize_window()
        f.Text_Mixto_Validado("xpath", "//input[@id='user-name']", email, 1)
        f.Text_Mixto_Validado("xpath", "//input[@id='password']", clave, 1)
        f.Click_Mixto("xpath", "//input[@id='login-button']", 1)
        e1 = f.SEX("//div[@class='app_logo']")
        e1 = e1.text
        if (e1 == mensaje):
            print("Prueba de validacion exitosa, Entraste correctamente a la pag")
            # AL ENTRAR A LA PAG, HAGO CLICK MANUALMENTE EN ACEPTAR XQ NO ME DA SU XPATH PARA QUITARLO
        else:
            print("La prueba de validacion es incorrecta")

        time.sleep(tiempo)
        driver.close()