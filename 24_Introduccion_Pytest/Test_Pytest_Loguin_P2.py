import time
#funciones excel
#from Funciones_Excel import *

#import unittest
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
from AA_Libreria_Funciones_Globales.Page_loguinglobal import Page_Loguinglobal
from selenium.webdriver import ActionChains
import pytest #para importar la libreria pytest


def test_Loguin_1():
    global driver
    driver = webdriver.Chrome()
    f=Libreria_Funciones_Globales(driver) #IMPORTANTE NUNCA OLVIDAR EN EL (), colocar (driver)
    f.Navegar("https://www.saucedemo.com/",1)
    driver.maximize_window()
    f.Text_Mixto_Validado("xpath","//input[@id='user-name']","standard_user",1)
    f.Text_Mixto_Validado("xpath","//input[@id='password']","12345",1)
    f.Click_Mixto("xpath","//input[@id='login-button']",1)
    e1=f.SEX("//h3[@data-test='error']")
    e1=e1.text
    #print("Epic sadface: Username and password do not match any user in this service")
    if (e1=="Epic sadface: Username and password do not match any user in this service"):
        print("Prueba de validacion exitosa, debes colocar la contraseña correcta")
    else:
        print("La prueba de validacion es incorrecta")

    time.sleep(2)
    driver.close()

def test_Loguin_2():
    global driver
    driver = webdriver.Chrome()
    f=Libreria_Funciones_Globales(driver) #IMPORTANTE NUNCA OLVIDAR EN EL (), colocar (driver)
    f.Navegar("https://www.saucedemo.com/",1)
    driver.maximize_window()
    f.Text_Mixto_Validado("xpath","//input[@id='user-name']","",1)
    f.Text_Mixto_Validado("xpath","//input[@id='password']","12345",1)
    f.Click_Mixto("xpath","//input[@id='login-button']",1)
    e1=f.SEX("//h3[normalize-space()='Epic sadface: Username is required']")
    e1=e1.text
    #print("Epic sadface: Username and password do not match any user in this service")
    if (e1=="Epic sadface: Username is required"):
        print("Prueba de validacion exitosa, debes colocar el correo de usuario")
    else:
        print("La prueba de validacion es incorrecta")

    time.sleep(2)
    driver.close()

def test_Loguin_3():
    global driver
    driver = webdriver.Chrome()
    f=Libreria_Funciones_Globales(driver) #IMPORTANTE NUNCA OLVIDAR EN EL (), colocar (driver)
    f.Navegar("https://www.saucedemo.com/",1)
    driver.maximize_window()
    f.Text_Mixto_Validado("xpath","//input[@id='user-name']","Eduardo",1)
    f.Text_Mixto_Validado("xpath","//input[@id='password']","secret_sauce",1)
    f.Click_Mixto("xpath","//input[@id='login-button']",1)
    e1=f.SEX("//h3[contains(text(),'Epic sadface: Username and password do not match a')]")
    e1=e1.text
    #print("Epic sadface: Username and password do not match any user in this service")
    if (e1=="Epic sadface: Username and password do not match any user in this service"):
        print("Prueba de validacion exitosa, debes colocar correctamente el correo usuario")
    else:
        print("La prueba de validacion es incorrecta")

    time.sleep(2)
    driver.close()

def test_Loguin_4():
    global driver
    driver = webdriver.Chrome()
    f=Libreria_Funciones_Globales(driver) #IMPORTANTE NUNCA OLVIDAR EN EL (), colocar (driver)
    f.Navegar("https://www.saucedemo.com/",1)
    driver.maximize_window()
    f.Text_Mixto_Validado("xpath","//input[@id='user-name']","visual_user",1)
    f.Text_Mixto_Validado("xpath","//input[@id='password']","secret_sauce",1)
    f.Click_Mixto("xpath","//input[@id='login-button']",1)
    e1=f.SEX("//div[@class='app_logo']")
    e1=e1.text
    if (e1=="Swag Labs"):
        print("Prueba de validacion exitosa, Entraste correctamente a la pag")
        #AL ENTRAR A LA PAG, HAGO CLICK MANUALMENTE EN ACEPTAR XQ NO ME DA SU XPATH PARA QUITARLO
    else:
        print("La prueba de validacion es incorrecta")

    time.sleep(2)
    driver.close()