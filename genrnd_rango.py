from genrnd import fun_genrnd as genrnd

def ing2i():
    print("\nFuncion Ing2i")
    num1=int(input("\ningrese el primer numero: "))
    num2=int(input("ingrese el segundo numero: "))
    print("Los numeros ingresados son: ",num1," y ", num2)
    return

def ing2s():
    print("\nFuncion Ing2s")
    str1=str(input("\ningrese string 1 : "))
    str2=str(input("ingrese string 2 : "))
    print("Los String ingresados son: ",str1," y ", str2)
    return

def cartel_genrnd_range():
    """Cartel Ejercicio 18"""     
    print("---------------------------------------------------------------------")
    print("Punto 18: - función que calcule el rango del vector obtenido en genrnd")
    print("---------------------------------------------------------------------")




 # retorna una lista con 50 números aleatorios.
print("\n***Retorna una lista con 50 números aleatorios***")
list50=genrnd()
#print(list50)



# tira Error: 'list' object cannot be interpreted as an integer
# Rango del vector

def rango(lista):
 rango_valor = range(lista)
 return rango_valor
    
print("El rango del vector es:", rango(list50)) 