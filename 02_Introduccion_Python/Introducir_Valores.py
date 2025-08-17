#input

print("Cual es tu nombre :")
nom=input()
print("Cual es tu apellido paterno :")
ap=input()
print("Cual es tu apellido materno :")
am=input()

print("Dame el valor de A: ")
a=input()
a=int(a)

print("Dame el valor de B: ")
b=input()
b=int(b)
suma=a+b

print("Tu nombre es: {} {} {}".format(nom,ap,am))
print("La suma de {} + {} = {}".format(a,b,suma))

