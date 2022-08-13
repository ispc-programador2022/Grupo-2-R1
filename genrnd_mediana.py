from genrnd import fun_genrnd as genrnd
from statistics import median


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

def cartel_genrnd_mediana():
    """Cartel Ejercicio 17"""     
    print("\n---------------------------------------------------------------------")
    print("Punto 17: función que calcule la mediana del vector obtenido en genrnd")
    print("---------------------------------------------------------------------")

    
    
# Mediana de la lista
def fun_mediana(): 
    """
    ***Retorna una lista con 50 números aleatorios***
    """
    list50=genrnd()  
    mediana_valor = median(list50)
    print("\nla mediana del vector es:", mediana_valor) 
    return mediana_valor
    


if __name__ == "__main__":
    ing2i()
    ing2s() 
    cartel_genrnd_mediana()
    fun_mediana()