print("Retorna el producto de los dos primeros parametros mas el tercer parametro,usando las funciones anteriores")
from producto import producto  


def funcion_p1_producto (a,b,num3):

 funcion_p1_producto=producto(a,b)+num3
 print("El resultado total es: ",funcion_p1_producto)
 return funcion_p1_producto

a=int((input("Ingresar el primer valor: ")))

b=int((input("Ingresar el segundo valor: ")))
producto(a,b)
num3=int(input("I2ngrese el tercer valor: "))
funcion_p1_producto(a,b,num3)
