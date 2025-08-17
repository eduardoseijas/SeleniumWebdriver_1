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
        f.Navegar("https://demoqa.com/text-box",1)
        f.Text_Mixto_Validado("xpath","//input[@id='userName']","Eduardo",2)
        f.Text_Mixto_Validado("id","userEmail","Eduardoseijas@hotmail.com",2)
        f.Text_Mixto_Validado("css","#currentAddress","direcc1",2)
        f.Click_Mixto("css","#submit",2)