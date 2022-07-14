
from suma import suma


def funcion_p1_suma (a,b,num3):
  
 funcion_p1_suma=suma(a,b)*num3
 print("El resultado total es: ",funcion_p1_suma)
 return funcion_p1_suma

a=int((input("Ingresar el primer valor: ")))

b=int((input("Ingresar el segundo valor: ")))
suma(a,b)
num3=int(input("Ingrese el tercer valor: "))
funcion_p1_suma(a,b,num3)


	
