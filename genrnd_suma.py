from genrnd import fun_genrnd as genrnd
from itertools import combinations

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


def cartel_genrnd_suma():
    """Cartel Ejercicio 13"""     
    print("\n---------------------------------------------------------------------")
    print("Punto 13: función que devuelva la suma de las combinaciones posibles")
    print("de los números generados por la función genrnd tomados de a dos")
    print("---------------------------------------------------------------------")


def fun_genrnd_suma():
    """Busca combinaciones posibles de genrnd tomados de a dos"""
    """Y devuelve la suma las combinaciones"""   
    genrnd_comb = list(combinations(genrnd(),2))
    total_suma = sum(list(map(sum, list(genrnd_comb))))
    print("\nSuma total de las combinaciones posibles: ", total_suma)
    return fun_genrnd_suma


if __name__ == "__main__":
    ing2i()
    ing2s()
    cartel_genrnd_suma() 
    fun_genrnd_suma()  
    