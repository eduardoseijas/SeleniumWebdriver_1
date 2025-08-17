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

@pytest.mark.run
def test_Validar_If():
    print("Primer test")
    assert True

@pytest.mark.run
def test_dos():
    a=10
    b=10
    assert a==b, "no son iguales"

@pytest.mark.run
def test_tres():
    a=5
    b=10
    assert a==b, "no son iguales"

@pytest.mark.run
def test_cuatro():
    a=15
    b=10
    assert a>b, "A no es mayor que B"

@pytest.mark.run
def test_cinco():
    nom="Eduardo"

    assert nom=="Eduard", "Nombre no es rodrigo"