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
from AA_Libreria_Funciones_Globales.Libreria_Funciones import Libreria_Funciones_Globales
from AA_Libreria_Funciones_Globales.Page_loguinglobal import Page_Loguinglobal
from selenium.webdriver import ActionChains

class PruebaLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login1(self,):
        driver=self.driver
        f=Libreria_Funciones_Globales(driver)
        f.Navegar("https://validaciones.rodrigovillanueva.com.mx/Botones_ok.html",2)
        f.Text_Xpath_Validando("//input[@id='nombre']","Eduardo",2)
        f.Mouse_DobleClick("xpath","//button[normalize-space()='Doble Click Me']",3)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()