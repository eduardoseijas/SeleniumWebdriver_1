#Fuciones con *args / *args, significa que puede tener Nº cantidad de valores

def suma(*args):
    resultado=0
    for n in args:
        resultado=resultado+n
    print("El resultado es: "+str(resultado))

suma(5,9)



