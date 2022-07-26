print("Retorna la resta de los dos primeros parametros por el tercer parametro,usando las funciones anteriores")
from resta import resta  


def funcion_p1_resta (a,b,num3):
  
 funcion_p1_resta=resta(a,b)*num3
 print("El resultado total es: ",funcion_p1_resta)
 return funcion_p1_resta

a=int((input("Ingresar el primer valor: ")))

b=int((input("Ingresar el segundo valor: ")))
resta(a,b)
num3=int(input("Ingrese el tercer valor: "))
funcion_p1_resta(a,b,num3)
