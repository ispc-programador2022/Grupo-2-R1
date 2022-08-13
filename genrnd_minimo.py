from genrnd import fun_genrnd as genrnd

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

def cartel_genrnd_min():
    """Cartel Ejercicio 20"""
    print("\n-----------------------------------------------")
    print("punto 20: función que calcule devuelva el minimo")
    print("del vector obtenido en genrnd")
    print("----------------------------------------------")




# Minimo de la lista
def minimo():
    # retorna una lista con 50 números aleatorios.
    list50=genrnd()
    minimo_valor = min(list50)
    print("\nel valor minimo es:", minimo_valor) 
    return minimo_valor
    

if __name__ == "__main__":
    ing2i()
    ing2s() 
    cartel_genrnd_min()
    minimo()