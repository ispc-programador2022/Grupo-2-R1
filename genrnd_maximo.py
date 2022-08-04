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

def cartel_genrnd_max():
    """Cartel Ejercicio 21"""
    print("-----------------------------------------------")
    print("Punto 21: función que calcule devuelva el maximo del vector ")
    print(" del vector obtenido en genrnd")
    print("----------------------------------------------")

 

# Maximo de la lista
def maximo():
    # retorna una lista con 50 números aleatorios.
    list50= genrnd()
    maximo_valor = max(list50)
    print("el valor maximo es:", maximo_valor) 
    return maximo_valor
    
    
if __name__ == "__main__":
    ing2i()
    ing2s() 
    cartel_genrnd_max()
    maximo()