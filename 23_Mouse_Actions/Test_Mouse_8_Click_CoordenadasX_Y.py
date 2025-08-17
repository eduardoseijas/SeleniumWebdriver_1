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
        f.Navegar("https://jqueryui.com/draggable/",2)
        f.Click_Mixto_X_Y("xpath","//a[normalize-space()='Demos']",300,0,4)

#Como google no me permitia use la pag perplexity, es similar para el ejercicio
    def test_Google_CoordenadasX_Y(self,):
        driver=self.driver
        f=Libreria_Funciones_Globales(driver)
        f.Navegar("https://www.perplexity.ai/",3)
        f.Text_Mixto_Validado("xpath","//div[@id='ask-input']//p","fer",3)
        f.Click_Mixto_X_Y("xpath","//div[@id='ask-input']//p",0,120,3)






    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()