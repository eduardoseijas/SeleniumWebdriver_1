a=400
b=500
c=100

if(a>b and a>c):
    print("El mayor es: "+str(a))
elif(b>a and b>c):
    print("El mayor es "+str(b))
elif(c>a and c>b):
    print("El mayor es "+str(b))

if(a<b or a>c):
    print("{} es menor que {} ó mayor que {} ".format(a,b,a,c))
