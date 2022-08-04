import random


def ing2i():
    print("Comencemos con nuestro viaje...")
    numero1=int(input("\nPor favor ingrese el primer numero entero: "))
    numero2=int(input("Por favor ingrese el segundo numero entero: "))
    print("\nLos numeros ingresados son: ",numero1, numero2)
    
def ing2s():
    str1=str(input("\nPor favor ingrese el primer valor string: "))
    str2=str(input("Por favor ingrese el segundo valor string: "))
    print("\nLos valores string ingresados son: ",str1, str2)


def cartel_genrnd2():
    """Cartel Ejercicio 22"""
    print("\n-----------------------------------------------")
    print("Punto 22: función genrnd que retorna una lista")
    print("          con 500.000.000.000.000.000 números aleatorios")
    print("----------------------------------------------")
    print("  ")


def fun_genrnd2():   
    """Genera 500.000.000.000.000.000 numeros random entre 0 y 500.000.000.000.000.000"""   
    return list(random.randint(1,9)for x in range (500000000000000000))


if __name__ == "__main__":
    ing2i()
    ing2s()
    cartel_genrnd2()
    fun_genrnd2()