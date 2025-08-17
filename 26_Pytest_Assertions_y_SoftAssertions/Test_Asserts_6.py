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

driver = ""
f = ""

@pytest.fixture(scope='module')
def setup_login():
    global driver,f
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    f = Libreria_Funciones_Globales(driver)
    f.Text_Mixto_Validado("xpath","//input[@id='user-name']","standard_user",1)
    f.Text_Mixto_Validado("xpath","//input[@id='password']","secret_sauce",1)
    f.Click_Xpath("//input[@id='login-button']",1)


    time.sleep(1)
    print("Iniciando nuestros Test")


def teardown_function():
    print("Fin de los test")
    driver.close()

@pytest.mark.login
@pytest.mark.usefixtures("setup_login")
def test_uno_Assert1():
    f = Libreria_Funciones_Globales(driver)
    etiqueta=f.SEX("//div[@class='app_logo']").text
    print(etiqueta)
    if(etiqueta== "Swag Labs"): #cambiar este tambien
        print("Adentro")
        assert etiqueta== "Swag Labs"

    else:
        print("Afuera")
        assert etiqueta== "Swag Labs", "No entro a la pag de inicio" #tiene que ser diferente aqui para
                                                                     #que funcione la doble validacion
