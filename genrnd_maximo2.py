from genrnd2 import fun_genrnd2 as genrnd2

def cartel_genrnd_maximo2():
    """Cartel Ejercicio 21"""
    print("-----------------------------------------------")
    print("Punto 22: función que calcule devuelva el maximo del vector ")
    print(" del vector obtenido en genrnd")
    print("----------------------------------------------")
    print("  ")

 # retorna una lista con 50 números aleatorios.
print("\n***Retorna una lista con 500.000.000.000.000.000 números aleatorios***")
listaa= genrnd2()
#print(listaa)

# Maximo de la lista
def maximo2(lista):
 maximo_valor2 = max(lista)
 return maximo_valor2
    
print("el valor maximo es:", maximo2(listaa)) 
