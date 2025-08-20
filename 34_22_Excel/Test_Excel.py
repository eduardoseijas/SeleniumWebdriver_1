import time
import unittest
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
from AA_Libreria_Funciones_Globales.Page_loguinglobal import Page_Loguinglobal
import openpyxl
from Funciones_Excel import * #esta es las funciones que esta en la carpeta 34

class base_test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def test_1(self):
        driver=self.driver
        f=Libreria_Funciones_Globales(driver)
        fe=Funexcel(driver)
        f.Navegar("https://validaciones.rodrigovillanueva.com.mx/Form1.html",1)
        ruta="C://Practica_Selenium_2//34_22_Excel//Selenium.xlsx"
        #DEBE IR EN DOBLE / -> //
        #QUITAR LA QUE VIENE CUANDO COPIAS LA RUTA -> \
        filas=fe.getRowCount(ruta,"Hoja1")

        for n in range (2,filas+1):
            nombre=fe.readData(ruta,"Hoja1",n,1)
            apellido=fe.readData(ruta,"Hoja1",n,2)
            email=fe.readData(ruta,"Hoja1",n,3)
            Tlf=fe.readData(ruta,"Hoja1",n,4)
            Direccion = fe.readData(ruta, "Hoja1", n, 5)

            f.Text_Mixto_Validado("xpath","//input[@id='nombre']",nombre,1)
            f.Text_Mixto_Validado("xpath", "//input[@id='apellidos']", apellido, 1)
            f.Text_Mixto_Validado("xpath", "//input[@id='email']", email, 1)
            f.Text_Mixto_Validado("xpath", "//input[@id='tel']", Tlf, 1)
            f.Text_Mixto_Validado("xpath", "//input[@id='direccion']", Direccion, 1)
            f.Click_Xpath("//button[@type='submit']",1)

            e=f.Existe("xpath","//input[@id='nombre']",1)
            if(e=="Existe"):
                print("El elemento se inserto correctamente")
                fe.writeData(ruta,"Hoja1",n,5,"demo cuatro")
            else:
                print("No se inserto")
                fe.writeData(ruta,"Hoja1",n,5,"Error")


