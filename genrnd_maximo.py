from genrnd import fun_genrnd as genrnd

def cartel_genrnd_maximo():
    """Cartel Ejercicio 21"""
    print("-----------------------------------------------")
    print("Punto 21: función que calcule devuelva el maximo del vector ")
    print(" del vector obtenido en genrnd")
    print("----------------------------------------------")
    print("  ")

 # retorna una lista con 50 números aleatorios.
print("\n***Retorna una lista con 50 números aleatorios***")
list50= fun_genrnd()
print(list50)

# Maximo de la lista
def maximo(lista):
 maximo_valor = max(lista)
 return maximo_valor
    
print("el valor maximo es:", maximo(list50)) 
