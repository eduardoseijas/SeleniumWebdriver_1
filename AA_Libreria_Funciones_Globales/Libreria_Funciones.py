import time
import unittest
from datetime import timezone
from os import times
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
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

class Libreria_Funciones_Globales():

    def __init__(self,driver):
        self.driver=driver


    #Funcion de tiempo
    def Tiempo(self,Tiempo):
        t=time.sleep(Tiempo)
        return t

    #Funcion de la pag web
    def Navegar(self,Url,Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Pagina Abierta: " +str(Url))
        t=time.sleep(Tiempo)
        return t


    #Funcion Text con Xpath
    def Text_Xpath(self,xpath,texto,tiempo):
        val=self.driver.find_element(By.XPATH,xpath)
        val.clear()
        val.send_keys(texto)
        t=time.sleep(tiempo)
        return t

    def Text_Xpath_Validando(self,xpath,texto,tiempo):
        try:
            val=WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val=self.driver.find_element(By.XPATH,xpath)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo{} el texto -> {} : ".format(xpath,texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + xpath)


    #Funcion Text con ID
    def Text_ID(self,id,texto,tiempo):
        val=self.driver.find_element(By.ID, id)
        val.clear()
        val.send_keys(texto)
        t=time.sleep(tiempo)
        return t

    def Text_ID_Validando(self,id,texto,tiempo):
        try:
            val=WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val=self.driver.find_element(By.ID,id)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo{} el texto -> {} : ".format(id, texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + id)

    #Funcion Text con CSS
    def Text_CSS_Validando(self,css,texto,tiempo):
        try:
            val=WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,css)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val=self.driver.find_element(By.CSS_SELECTOR,css)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo{} el texto -> {} : ".format(css, texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + css)

    def SEX(self,elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    def SEI(self,elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, elemento)
        return val

    def SECCS(self,elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.CSS_SELECTOR, elemento)
        return val

    def Text_Mixto_Validado(self,tipo, selector, texto, tiempo):
        if (tipo== "xpath"):
            try:
                val=self.SEX(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo{} el texto -> {} : ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)
        elif(tipo=="id"):
            try:
                val = self.SEI(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo{} el texto -> {} : ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)

        elif (tipo == "css"):
            try:
                val=self.SECCS(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo{} el texto -> {} : ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)


    #Funcion Click
    def Click_Xpath(self,xpath,tiempo):
        try:
            val=WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val=self.driver.find_element(By.XPATH,xpath)
            val.click()
            print("Hacemos click en el campo {}: ".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + xpath)

    def Click_ID(self, id, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID,id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID,id)
            val.click()
            print("Hacemos click en el campo {}: ".format(id))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + id)

    def Click_CSS(self, css, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,css)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.CSS_SELECTOR, css)
            val.click()
            print("Hacemos click en el campo {}: ".format(css))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + css)

    #Click mixto
    def Click_Mixto(self,tipo,selector, tiempo):
        if(tipo=="xpath"):
            try:
                val = self.SEX(selector)
                val.click()
                print("Hacemos click en el campo {}: ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val.click()
                print("Hacemos click en el campo {}: ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)
        elif (tipo == "css"):
            try:
                val = self.SECCS(selector)
                val.click()
                print("Hacemos click en el campo {}: ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)

    #Click mixto con Coordenadas
    def Click_Mixto_X_Y(self,tipo,selector,x,y, tiempo):
        if(tipo=="xpath"):
            try:
                val = self.SEX(selector)
                act=ActionChains(self.driver)
                act.move_to_element_with_offset(val,x,y).click().perform()
                print("Hacemos click en el elemento {} en las coordenadas {}, {}  ".format(selector,x,y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Hacemos click en el elemento {} en las coordenadas {}, {}  ".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)
        elif (tipo == "css"):
            try:
                val = self.SECCS(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Hacemos click en el elemento {} en las coordenadas {}, {}  ".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)

    #Funcion - Select Con las tres posiible: texto, value, index
    def Select_Xpath_Type(self,xpath,tipo,dato,tiempo):
        try:
            val=self.SEX(dato)
            val=Select(val)
            if(tipo=="text"):
                val.select_by_visible_text(dato)
            elif(tipo=="index"):
                val.select_by_index(dato)
            elif(tipo=="value"):
                val.select_by_value(dato)
            print("El campo seleccionado es: {}" .format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + xpath)

    def Select_ID_Type(self,id,tipo,dato,tiempo):
        try:
            val=self.SEI(dato)
            val=Select(val)
            if(tipo=="text"):
                val.select_by_visible_text(dato)
            elif(tipo=="index"):
                val.select_by_index(dato)
            elif(tipo=="value"):
                val.select_by_value(dato)
            print("El campo seleccionado es: {}" .format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + id)

    #Funcion Des-Select Con las tres posiible: texto, value, index
    def DeSelect_Xpath_Type(self,xpath,tipo,dato,tiempo):
        try:
            val=self.SEX(dato)
            if(tipo=="text"):
                val.deselect_by_visible_text(dato)
            elif(tipo=="index"):
                val.deselect_by_index(dato)
            elif(tipo=="value"):
                val.deselect_by_value(dato)
            print("El campo De-Seleccionado es: {}" .format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + xpath)

    def DeSelect_ID_Type(self,id,tipo,dato,tiempo):
        try:
            val=self.SEI(dato)
            val=Select(val)
            if(tipo=="text"):
                val.deselect_by_visible_text(dato)
            elif(tipo=="index"):
                val.deselect_by_index(dato)
            elif(tipo=="value"):
                val.deselect_by_value(dato)
            print("El campo De-Seleccionado es: {}" .format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + id)

    #Cargar imagenes
    def Upload_file_Xpath(self,xpath,ruta,tiempo):
        try:
            val=self.SEX(ruta)
            val.send_keys(ruta)
            print("Se carga la imagen {}" .format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + xpath)

    def Upload_file_ID(self, id, ruta, tiempo):
        try:
            val = self.SEI(ruta)
            val.send_keys(ruta)
            print("Se carga la imagen {}".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + id)

    #Funcion para Radio y Checks
    def Check_Xpath(self, xpath,tiempo):
        try:
            val = self.SEX(xpath)
            val.click()
            print("Hace Click en el elemento {}".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + xpath)

    def Check_ID(self, id,tiempo):
        try:
            val = self.SEI(id)
            val.click()
            print("Hace Click en el elemento {}".format(id))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro, el elemento:" + id)

    #Check Multiple
    def Check_Xpath_Multiples(self,tiempo,*args):
        try:
            for num in args:
                val = self.SEX(num)
                val.click()
                print("Hace Click en el elemento {}".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontro, el elemento:" + num)

    #Mouse Doble Clcik
    def Mouse_DobleClick(self,tipo, selector, tiempo):
        if (tipo== "xpath"):
            try:
                val = self.SEX(selector)
                act=ActionChains(self.driver)
                act.double_click(val).perform()
                print("DobleClick en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)
        elif(tipo=="id"):
            try:
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("DobleClick en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)

        elif (tipo == "css"):
            try:
                val = self.SECCS(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("DobleClick en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)

    #Mouse Click Boton derecho .contex_click().perform()
    def Mouse_Click_BotonDerecho(self,tipo, selector, tiempo):
        if (tipo== "xpath"):
            try:
                val = self.SEX(selector)
                act=ActionChains(self.driver)
                act.context_click(val).perform()
                print("DobleClick en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)
        elif(tipo=="id"):
            try:
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Hiciste click al boton derecho en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)

        elif (tipo == "css"):
            try:
                val = self.SECCS(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Hiciste click al boton derecho en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)


    #Mouse Drag And Drop
    def Mouse_DragAndDrop(self,tipo, selector,destino, tiempo):
        if (tipo== "xpath"):
            try:
                val = self.SEX(selector)
                val2=self.SEX(destino)
                act=ActionChains(self.driver)
                act.drag_and_drop(val,val2).perform()
                print("Se solto el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)
        elif(tipo=="id"):
            try:
                val = self.SEI(selector)
                val2= self.SEI(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val,val2).perform()
                print("Hiciste click al boton derecho en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)

        elif (tipo == "css"):
            try:
                val = self.SECCS(selector)
                val2 = self.SECCS(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val,val2).perform()
                print("Hiciste click al boton derecho en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)


    #Mouse Drag And Drop Por Coordenadas X,Y
    def Mouse_DragAndDrop_X_Y(self,tipo, selector,x,y, tiempo):
        if (tipo== "xpath"):
            try:
                self.driver.switch_to.frame(0) #Funcion para los iframe
                val = self.SEX(selector)
                act=ActionChains(self.driver)
                act.drag_and_drop_by_offset(val,x,y).perform()
                print("Se solto el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)
        elif(tipo=="id"):
            try:
                self.driver.switch_to.frame(0)  # Funcion para los iframe
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val,x,y).perform()
                print("Hiciste click al boton derecho en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)

        elif (tipo == "css"):
            try:
                self.driver.switch_to.frame(0)  # Funcion para los iframe
                val = self.SECCS(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop(val,x,y).perform()
                print("Hiciste click al boton derecho en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)

    #Limpiador
    def Clear(self,tipo,selector,tiempo):
        if (tipo== "xpath"):
            try:
                val = self.SEX(selector)
                val.clear()
                print("El elemento {} se ha limpiado ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)
        elif(tipo=="id"):
            try:
                val = self.SEI(selector)
                val.clear()
                print("El elemento {} se ha limpiado".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)

        elif (tipo == "css"):
            try:
                val = self.SECCS(selector)
                val.clear()
                print("El elemento {} se ha limpiado".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro, el elemento:" + selector)


    #salida
    def Salida(self):
        print("Se termina la prueba exitosamete")