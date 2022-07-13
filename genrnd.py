import random


def cartel_genrnd():
    """Cartel Ejercicio 12"""
    print("-----------------------------------------------")
    print("Punto 12: función genrnd que retorna una lista")
    print("          con 50 números aleatorios")
    print("----------------------------------------------")
    print("  ")


def fun_genrnd():   
    """Genera 50 numeros random entre 0 y 50"""   
    return list(random.randint(0,50)for x in range (50))


if __name__ == "__main__":
    cartel_genrnd()
    print(fun_genrnd())
    print(" ")