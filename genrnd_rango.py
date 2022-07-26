from genrnd import fun_genrnd as genrnd
from itertools import combinations
import statistics

def cartel_genrnd_range():
    """Cartel Ejercicio 18"""     
    print("---------------------------------------------------------------------")
    print("Punto 18: - función que calcule el rango del vector obtenido en genrnd")
    print("---------------------------------------------------------------------")
    print(" ")

 # retorna una lista con 50 números aleatorios.
print("\n***Retorna una lista con 50 números aleatorios***")
list50=genrnd()
print(list50)

# Rango del vector
def rango(lista):
 rango_valor = range(lista)
 return rango_valor
    
print("El rango del vector es:", rango(list50)) 