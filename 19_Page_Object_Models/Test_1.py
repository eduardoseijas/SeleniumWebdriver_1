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



    #def test_login1(self):
        #driver=self.driver
        #f=Funciones_Globales(driver)
        #f.Navegar("https://www.saucedemo.com/",1)
        #f.Tiempo(2)
        #f.Text_Xpath_Validando("//input[@id='user-name']","Eduardo",1)
        #f.Text_CSS_Validando("#password","1234",1)
        #f.Click_CSS("#login-button",1)

    def test_login1(self):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://validaciones.rodrigovillanueva.com.mx/ComboBox_ok.html",1)
        f.Select_Xpath_Type("(//select[@id='comboBox2'])[1]","text","Valor 1",1)
        f.Select_Xpath_Type("(//select[@id='comboBox2'])[1]","index",2,1)
        f.Select_Xpath_Type("(//select[@id='comboBox2'])[1]","value","2",1)
        f.DeSelect_Xpath_Type("(//select[@id='comboBox2'])[1]","text","Valor 1",1)
        f.DeSelect_Xpath_Type("(//select[@id='comboBox2'])[1]", "index", 2, 1)
        f.DeSelect_Xpath_Type("(//select[@id='comboBox2'])[1]", "value", "2", 1)
        f.Select_ID_Type("comboBox2","text","Valor 1",1)
        f.Select_ID_Type("comboBox2","index",2,1)
        f.Select_ID_Type("comboBox2","value","2",1)
        f.DeSelect_ID_Type("comboBox2","text","Valor 1",1)
        f.DeSelect_ID_Type("comboBox2","index",2,1)
        f.DeSelect_ID_Type("comboBox2","value","2",1)










    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__=='__main__':
    unittest.main()