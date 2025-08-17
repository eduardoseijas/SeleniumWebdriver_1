import time
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
from Funciones.Funciones import Funciones_Globales

class Page_Loguin1():

    def __init__(self,driver):
        self.driver=driver

    def Loguin_Master(self, url, name, clave, t):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar(url,t)
        f.Tiempo(t)
        f.Text_Xpath_Validando("//input[@id='user-name']",name,t)
        f.Text_Xpath_Validando("//input[@id='password']",clave,t)
        f.Click_Xpath("//input[@id='login-button']",1)
        f.Salida()


