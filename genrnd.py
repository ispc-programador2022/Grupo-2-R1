import random

def ing2i():
    """
    función ing2i, debe permitir el ingreso de 2 valores enteros
    """
    print("\nFuncion Ing2i")
    num1=int(input("\ningrese el primer numero: "))
    num2=int(input("ingrese el segundo numero: "))
    print("Los numeros ingresados son: ",num1," y ", num2)
    return

def ing2s():
    """
    función ing2s, debe permitir el ingreso de 2 valores string
    """
    print("\nFuncion Ing2s")
    str1=str(input("\ningrese string 1 : "))
    str2=str(input("ingrese string 2 : "))
    print("Los String ingresados son: ",str1," y ", str2)
    return

def cartel_genrnd():
    """Cartel Ejercicio 12"""
    print("\n-----------------------------------------------")
    print("Punto 12: función genrnd que retorna una lista")
    print("          con 50 números aleatorios")
    print("----------------------------------------------")



def fun_genrnd():   
    """Genera 50 numeros random entre 1 y 9"""   
    return list(random.randint(1,9)for x in range (50))


if __name__ == "__main__":
    ing2i()
    ing2s()
    cartel_genrnd()
    fun_genrnd()