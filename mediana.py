from genrnd import fun_genrnd as genrnd
from itertools import combinations
import statistics

def cartel_genrnd_mediana():
    """Cartel Ejercicio 17"""     
    print("---------------------------------------------------------------------")
    print("Punto 17: función que calcule la mediana del vector obtenido en genrnd")
    print("---------------------------------------------------------------------")
    print(" ")

    # retorna una lista con 50 números aleatorios.
print("\n***Retorna una lista con 50 números aleatorios***")
list50 = genrnd(50)
print(list50)
    
    
    # Mediana de la lista
print("\n***Devuelve la mediana de la lista aleatorea***")
print("Mediana= ",statistics.median(list50))
