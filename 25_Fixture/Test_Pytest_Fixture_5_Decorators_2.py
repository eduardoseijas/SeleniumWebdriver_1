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
from AA_Libreria_Funciones_Globales.Page_loguinglobal import Page_Loguinglobal

driver=""
f= ""

@pytest.fixture(scope='module')

def setup_loguin_uno():
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    f=Libreria_Funciones_Globales(driver)
    f.Text_Mixto_Validado("id", "user-name", "standard_user", 1)
    f.Text_Mixto_Validado("id", "password", "secret_sauce", 1)
    f.Click_Mixto("xpath", "//input[@id='login-button']", 1)
    time.sleep(1)
    print("Entrando al sistema")
    yield
    print("Salida del loguin sauce")


@pytest.fixture(scope='module')
def setup_loguin_dos():
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    f=Libreria_Funciones_Globales(driver)
    f.Text_Mixto_Validado("xpath","//input[@placeholder='Username']","Admin",1)
    f.Text_Mixto_Validado("xpath","//input[@placeholder='Password']","admin123",1)
    f.Click_Mixto("xpath","//button[@type='submit']",1)
    time.sleep(1)
    print("Entrando al sistema")
    yield
    print("Salida del loguin uno")


@pytest.mark.usefixtures("setup_loguin_uno")
def test_uno():
    print("Entrando al sistema uno")
    f=Libreria_Funciones_Globales(driver)
    f.Click_Mixto("xpath","//img[@alt='Sauce Labs Backpack']",1)
    f.Click_Mixto("xpath","//button[@id='add-to-cart']",1)
    f.Click_Mixto("xpath","//button[@id='back-to-products']",1)
    f.Click_Mixto("xpath", "//img[@alt='Sauce Labs Bike Light']", 1)
    f.Click_Mixto("xpath", "//button[@id='back-to-products']", 1)
    f.Click_Mixto("xpath", "//img[@alt='Test.allTheThings() T-Shirt (Red)']", 1)
    f.Click_Mixto("xpath","//button[@id='add-to-cart']",1)
    f.Click_Mixto("xpath","//a[@class='shopping_cart_link']",1)
    f.Click_Mixto("xpath","//button[@id='checkout']",1)
    f.Text_Mixto_Validado("xpath","//input[@id='first-name']","Eduardo",1)
    f.Text_Mixto_Validado("id","last-name","Pacheco",1)
    f.Text_Mixto_Validado("id","postal-code","45600",1)
    f.Click_Mixto("xpath","//input[@id='continue']",1)
    time.sleep(2)
    driver.close()


@pytest.mark.usefixtures("setup_loguin_dos")
def test_dos():
    print("Entrando al sistema dos")
    f=Libreria_Funciones_Globales(driver)
    f.Click_Mixto("xpath","//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']",1)
    f.Click_Mixto("xpath","//a[normalize-space()='Change Password']",1)
    f.Click_Mixto("xpath","//a[normalize-space()='Add Employee']",1)
    f.Text_Mixto_Validado("xpath","//input[@placeholder='First Name']","Eduardo",1)
    f.Text_Mixto_Validado("xpath","//input[@placeholder='Middle Name']","Alejo",1)
    f.Text_Mixto_Validado("xpath","//input[@placeholder='Last Name']","Paredes",1)
    f.Click_Mixto("xpath","//button[normalize-space()='Save']",2)
    time.sleep(2)
    driver.close()


