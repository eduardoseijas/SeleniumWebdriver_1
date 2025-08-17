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
from Funciones.Funciones import Funciones_Globales #de la carpeta Funciones y el archivo Funciones importame Funciones globales
from Page_Loguin import Page_Loguin1

class PruebaLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login1(self,):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://validaciones.rodrigovillanueva.com.mx/Radios_Ok.html",1)
        f.Check_Xpath("//input[@id='opcionA']",1)
        f.Check_ID("opcionB",1)
        f.Check_Xpath("//input[@id='opcionA']", 1)

    #Check Multiples
    def test_login2(self,):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://datatables.net/extensions/select/examples/checkbox/checkbox.html",1)
        for n in range(2,6):
            f.Check_Xpath_Multiples(2,"(//input[@aria-label='Select row'])["+str(n)+"]")
