Feature: Nuestro cuarto Demo

  ###Lanzando multiples casos

  Background:
    Given Abrimos el navegador en chrome - V2


Scenario Outline: Corriendo nuestro tercer test
      #Given Abrimos el navegador en chrome - V1
      When Cargamos los datos v2 "<user>" "<clave>"
      Then ingresamos a la pag chrome -v2
      And Seleccionamos el archivo en chrome -v2

  Examples:
  |             user              |    clave     |
  |         standard_user         | secret_sauce |
  |    Prueba bdd con examples    |   123456789  |

