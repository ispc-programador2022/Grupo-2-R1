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

def cartel_resta():
    """Cartel Ejercicio 2"""
    print("-----------------------------------------------")
    print("Punto 2: función resta, retorna la resta de 2 parámetros")
    print("----------------------------------------------")


def fun_resta():
    a=int((input("\nIngresar el primer valor: ")))
    b=int((input("Ingresar el segundo valor: ")))
    resta = a - b
    print("El resultado de la resta es: ",resta)
    return resta

if __name__ == "__main__":
    ing2i()
    ing2s()
    cartel_resta()
    fun_resta()
