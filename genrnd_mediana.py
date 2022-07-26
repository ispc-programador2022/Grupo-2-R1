from genrnd import fun_genrnd as genrnd
from itertools import combinations
from statistics import median

def cartel_genrnd_mediana():
    """Cartel Ejercicio 17"""     
    print("---------------------------------------------------------------------")
    print("Punto 17: función que calcule la mediana del vector obtenido en genrnd")
    print("---------------------------------------------------------------------")
    print(" ")
 # retorna una lista con 50 números aleatorios.
print("\n***Retorna una lista con 50 números aleatorios***")
list50=genrnd()
print(list50)

# Mediana de la lista
def mediana(lista):
 mediana_valor = median(lista)
 return mediana_valor
    
print("la mediana del vector es:", mediana(list50)) 