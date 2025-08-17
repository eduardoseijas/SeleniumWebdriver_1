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


#Al crear la class con el self.driver = webdriver.Chrome()
#No se debe colocar arriba junto con las librerias driver=webdriver.Chrome() porque te despliega una ventana vacia

class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        t = 2

    def test1(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")
        driver.maximize_window()
        time.sleep(4)


    def tearDown(self):
        driver.close()


if __name__=='__main__':
    unittest.main()