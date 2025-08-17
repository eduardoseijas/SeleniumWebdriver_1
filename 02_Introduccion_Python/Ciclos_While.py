'''

inicio=1
fin=10
while(inicio<=fin):
    print("Esto se repite: " +str(inicio))
    inicio=inicio+3
'''


#cuando colocas inicio=inicio1 o 2 o 3 o las que sean, es para que inicie y termine, si lo pones de 2 hace de 2 en 2, de 3, de 3 en 3
#iniciando siempre por el inicio q en este caso su valor en la variable era 1

inicio=1
fin=10
while(inicio<=fin):
    inicio=inicio+1
    if (inicio==6):
        continue
    print("Esto se repite "+str(inicio))