
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
    
def cartel_suma():
    """Cartel Ejercicio 1"""
    print("\n-----------------------------------------------")
    print("Punto 1: función suma, retorna la suma de 2 parámetros")
    print("----------------------------------------------")
    print("\nSe busca realizar la suma entre dos valores, a y b ")
    
def fun_suma():
    a=int((input("\nIngresar el primer valor: ")))
    b=int((input("Ingresar el segundo valor: ")))
    suma = a + b
    print("El resultado de la suma es: ",suma)
    return suma

if __name__ == "__main__":
    ing2i()
    ing2s()
    cartel_suma()
    fun_suma()
