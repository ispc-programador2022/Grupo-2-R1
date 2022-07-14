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
list50 = genrnd(50)
print(list50)
    
    # Rango de la lista
print("\n***Devuelve el rango de la lista aleatorea***")
print("Rango= ", range(list50))