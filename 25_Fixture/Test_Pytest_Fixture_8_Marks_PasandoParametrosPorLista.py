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



def get_Data():
    return [
        ("Rodrigo","12345"),
        ("Eduardo", "12345"),
        ("Pedro", "12345"),
        ("Lucia", "12345"),
        ("standard_user", "secret_sauce"),
    ]


@pytest.mark.login #para mandar a llamar la marca, por ejemplo desde la raiz
#python -m pytest .\25_Fixture\Test_Pytest_Fixture_8_Marks_PasandoParametrosPorLista.py -s -v -m login
@pytest.mark.parametrize("user,clave",get_Data())
def test_Loguin_Mark_Prueba(user,clave):
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    f=Libreria_Funciones_Globales(driver)
    f.Text_Mixto_Validado("id", "user-name", user, 1)
    f.Text_Mixto_Validado("id", "password", clave, 1)
    f.Click_Mixto("xpath", "//input[@id='login-button']", 1)
    time.sleep(1)

    print("Entrando al sistema")

def teardown_function(function):
    print("Salida del test")
    driver.close()

