import time
#funciones excel
#from Funciones_Excel import *
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
from selenium.webdriver import ActionChains
from behave import *
from AA_Libreria_Funciones_Globales.Libreria_Funciones import Libreria_Funciones_Globales
###USO LA LIBRERIA QUE TENGO A NIVEL GLOBAL Y FUNCIONA, PARA MIS FUNCIONES
driver =""
f=""

@given(u'Abrimos el navegador en chrome')
def step_impl(context):
    global driver,f
    context.driver=webdriver.Chrome()
    f=Libreria_Funciones_Globales(context.driver)
    f.Navegar("https://www.saucedemo.com/",1)

@when(u'Cargamos los datos del usuario chrome')
def step_impl(context):
    global driver, f
    f = Libreria_Funciones_Globales(context.driver)
    f.Text_Mixto_Validado("xpath","//input[@id='user-name']","standard_user",1)
    f.Text_Mixto_Validado("xpath", "//input[@id='password']", "secret_sauce", 1)
    f.Click_Mixto("xpath","//input[@id='login-button']",1)


@then(u'ingresamos a la pag chrome')
def step_impl(context):
    global driver, f
    f = Libreria_Funciones_Globales(context.driver)
    f.Click_Mixto("xpath", "//input[@id='login-button']", 1)


@then(u'Seleccionamos el archivo en chrome')
def step_impl(context):
    global driver, f
    f = Libreria_Funciones_Globales(context.driver)
    f.Click_Mixto("xpath", "// img[ @ alt = 'Sauce Labs Backpack']", 1)
    f.Click_Mixto("xpath","//button[@id='add-to-cart']",1)







