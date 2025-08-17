import time
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
driver=webdriver.Chrome()

t=2

driver.get("https://validaciones.rodrigovillanueva.com.mx/index.html")
driver.maximize_window()
time.sleep(t)

driver.find_element(By.XPATH,"//button[normalize-space()='Enviar']").click()
time.sleep(t)

name_val=driver.find_element(By.XPATH,"//div[@id='errorNombre']")
name=name_val.text
#print("El valor del error es: " + str(name))
if(name=="Nombre inválido, no puede estar vacio,mayor que 3 y tiene que ser Texto"):
    #print("Falta el nombre")
    cn=driver.find_element(By.XPATH,"//input[@id='nombre']")
    cn.send_keys("Eduardo")
    time.sleep(t)
    print("Nombre Correcto")
else:
    print("Falta el nombre")

ap_val=driver.find_element(By.XPATH,"//div[@id='errorApellidos']")
ap=ap_val.text
#print("El valor del error es: " + str(name))
if(ap=="Apellidos inválidos,, no puede estar vacio,mayor que 3 y tiene que ser Texto"):
    #print("Falta el nombre")
    cn=driver.find_element(By.XPATH,"//input[@id='apellidos']")
    cn.send_keys("Seijas Pacheco")
    time.sleep(t)
    print("Apellidos Correctos")
else:
    print("Faltan los Apellidos")

tlf_val=driver.find_element(By.XPATH,"//div[@id='errorTel']")
tlf=tlf_val.text
#print("El valor del error es: " + str(name))
if(tlf=="Teléfono inválido, no Puede estar vacio y tiene que ser un numero,tienen que ser 10 numeros"):
    #print("Falta el nombre")
    cn=driver.find_element(By.XPATH,"//input[@id='tel']")
    cn.send_keys("662555704")
    time.sleep(t)
    print("Telefono correcto")
else:
    print("Falta el telefono")

#Verificando que el boton esta disponible
print (driver.find_element(By.XPATH,"//button[normalize-space()='Enviar']").is_enabled())
if (driver.find_element(By.XPATH,"//button[normalize-space()='Enviar']").is_enabled()==True):
    print("Faltan Campos por llenar")
else:
    print("Listo todo, OK")
    time.sleep(t)
time.sleep(t)
driver.close()