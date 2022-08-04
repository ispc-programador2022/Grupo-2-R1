from genrnd import fun_genrnd as genrnd
import statistics


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

#crear la funcion del cartel
# y colocar el codigo dentro de una funcion

print("Funcion que calcula la media del vector obtenido en genrnd: ")
genrnd()
mean = statistics.mean(genrnd())
print("La media es: ",mean)


if __name__ == "__main__":
    ing2i()
    ing2s()
    #falta agregar el cartel del ejercicio 16
    # aca hay que agregar la funcion 16