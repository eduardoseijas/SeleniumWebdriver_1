Feature: Nuestro tercer Demo

  ###Hay una funcion que se llama Background: para no repetir

  Background:
    Given Abrimos el navegador en chrome - V1
    #dejo este y bloqueo los de abajo

  Scenario: Corriendo nuestro tercer test
     #Given Abrimos el navegador en chrome - V1
      When Cargamos los datos "standard_user" "secret_sauce"
      Then ingresamos a la pag chrome -v1
      And Seleccionamos el archivo en chrome -v1

    ####pasando parametros#####

    Scenario: Corriendo nuestro 4to test - fallido
     #Given Abrimos el navegador en chrome - V1
      When Cargamos los datos "juan" "1234567"
      Then ingresamos a la pag chrome -v1
      And Seleccionamos el archivo en chrome -v1

