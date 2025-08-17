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
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",1)
    driver.maximize_window()
    f.Clear("xpath","//input[@id='Email']",1)
    f.Text_Mixto_Validado("xpath","//input[@id='Email']","admin@yourstore.com",1)
    f.Clear("xpath","//input[@id='Password']",1)
    f.Text_Mixto_Validado("xpath","//input[@id='Password']","admin",1)
    f.Click_Mixto("xpath","//button[@type='submit']",1)
    time.sleep(2)
    driver.close()

