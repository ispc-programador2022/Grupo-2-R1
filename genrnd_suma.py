from genrnd import fun_genrnd as genrnd
from itertools import combinations


def cartel_genrnd_suma():
    """Cartel Ejercicio 13"""     
    print("---------------------------------------------------------------------")
    print("Punto 13: función que devuelva la suma de las combinaciones posibles")
    print("de los números generados por la función genrnd tomados de a dos")
    print("---------------------------------------------------------------------")
    print(" ")


def genrnd_suma():
    """Busca combinaciones posibles de genrnd tomados de a dos"""
    """Y devuelve la suma las combinaciones"""   
    genrnd_comb = list(combinations(genrnd(),2))
    total_suma = sum(list(map(sum, list(genrnd_comb))))
    return total_suma


if __name__ == "__main__":
    cartel_genrnd_suma()   
    print("Suma total de las combinaciones posibles: ", genrnd_suma())
    print(" ")