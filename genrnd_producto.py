from itertools import combinations
import random
import math


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

#Faltaria agregar la funcion del cartel

#no hace falta generar los numeros aleatorios
#la funcion fun_genrnd() del archivo gnrnd genera esos nums en una lista
#solo hay que importarla

num_rand = []

def genrnd(a, b):
    for i in range(50):
        num_rand.append(random.uniform(a,b))
        
def comb_prod(c):
    temp = combinations(c, 2)
    for i in list(temp):
        print(math.prod(i))
        
genrnd(100, 200)
print(num_rand)

comb_prod(num_rand)


if __name__ == "__main__":
    ing2i()
    ing2s()
    #aca hay que agregar el cartel 14
    #aca la funcion del ejercicio 14