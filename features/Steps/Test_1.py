from behave import *


#Pasos del Test_Uno de BDD Behave


@given(u'Abrimos el navegador')
def step_impl(context):
    print(u'Given Abrimos el navegador')


@when(u'Cargamos los datos del usuario')
def step_impl(context):
    print(u'When Cargamos los datos del usuario')


@then(u'ingresamos a la pag')
def step_impl(context):
    print(u'Then ingresamos a la pag')


@then(u'Seleccionamos el archivo')
def step_impl(context):
    print(u'Then Seleccionamos el archivo')
