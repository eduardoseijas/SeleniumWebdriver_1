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
f=""

#LA PAG WEB no permite seguir, no reconoce q sea humano y no me deja ingresar

def setup_function(function):
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    f=Libreria_Funciones_Globales(driver)
    f.Clear("id","Email",1)
    f.Clear("id", "Password", 1)
    f.Text_Mixto_Validado("id","Email","admin@yourstore.com",1)
    f.Text_Mixto_Validado("id","Password","admin",1)
    f.Click_Mixto("xpath","//button[@type='submit']",1)
    time.sleep(1)
    print("Iniciando nuestros Test")

def teardown_function(function):
    driver = webdriver.Chrome()
    print("Fin de los test")
    driver.close()

def test_uno():
    f=Libreria_Funciones_Globales(driver)
    f.Click_Mixto("xpath", "//p[normalize-space()='Catalog']", 2)
    f.Click_Mixto("xpath", "//p[normalize-space()='Products']", 2)
    f.Click_Mixto("xpath","//a[normalize-space()='Add new']",1)
    #driver.switch_to.frame(0)  # Funcion para los iframe

    time.sleep(1)
    driver.close()




