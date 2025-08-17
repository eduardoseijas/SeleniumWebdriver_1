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

def test_loguin_1_Con_PageLoguin():
    driver = webdriver.Chrome()
    fl=Page_Loguinglobal(driver)
    fl.Loguin_1("standard_user","12345","Epic sadface: Username and password do not match any user in this service",1)

def test_Loguin_2_Con_PagueLoguin():
    driver = webdriver.Chrome()
    fl = Page_Loguinglobal(driver)
    fl.Loguin_2("","12345","Epic sadface: Username is required",1)

def test_Loguin_3_Con_PagueLoguin():
    driver = webdriver.Chrome()
    fl = Page_Loguinglobal(driver)
    fl.Loguin_3("Eduardo","secret_sauce","Epic sadface: Username and password do not match any user in this service",2)

def test_Loguin_4_Con_PagueLoguin():
    driver = webdriver.Chrome()
    fl = Page_Loguinglobal(driver)
    fl.Loguin_4("standard_user","secret_sauce","Swag Labs",2)
    #Quite el mensaje que me sale en la pag manualmente

