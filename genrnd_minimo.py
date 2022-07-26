from genrnd import fun_genrnd as genrnd


def cartel_genrnd_minimo():
    """Cartel Ejercicio 20"""
    print("-----------------------------------------------")
    print("punto 20: función que calcule devuelva el minimo")
    print("del vector obtenido en genrnd")
    print("----------------------------------------------")
    print("  ")

 # retorna una lista con 50 números aleatorios.
print("\n***Retorna una lista con 50 números aleatorios***")
list50=genrnd()
print(list50)

# Minimo de la lista
def minimo(lista):
 minimo_valor = min(lista)
 return minimo_valor
    
print("el valor minimo es:", minimo(list50)) 
    
