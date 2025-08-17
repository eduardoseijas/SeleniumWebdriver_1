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
        f.Navegar("https://testpages.eviltester.com/styled/file-upload-test.html",1)
        f.Upload_file_Xpath("//input[@id='fileinput']","C:\Practica_Selenium_2//19_Page_Object_Models//ImagenesFunciones",1)
        f.Click_Xpath("//input[@id='itsanimage']",1)
        f.Click_Xpath("//input[@name='upload']",2)

    def test_login2(self,):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://testpages.eviltester.com/styled/file-upload-test.html", 1)
        f.Upload_file_ID("fileinput","C:\Practica_Selenium_2//19_Page_Object_Models//ImagenesFunciones",1)
        f.Click_ID("itsanimage",1)
        f.Click_CSS("input[value='Upload']",2)