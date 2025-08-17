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

@pytest.fixture(scope='module')
def setup_loguin_uno():
    print("Empezando el loguin del sistema uno")
    yield
    print("Saliendo del sistema prueba ok")

@pytest.fixture(scope='module')
def setup_loguin_dos():
    print("Empezando las pruebas del sistema dos")
    yield
    print("Fin de las pruebas del sistema dos")

def test_uno(setup_loguin_uno): #esta es una forma de llamarlo
    print("Empezando las pruebas del test uno########")

def test_dos(setup_loguin_dos):
    print("Esto es para la prueba dos#########")

@pytest.mark.usefixtures("setup_loguin_dos") #otra forma de llamarlo
def test_tres():
    print("Prueba tres del modulo loguin dos")