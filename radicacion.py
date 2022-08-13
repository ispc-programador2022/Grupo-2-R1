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

def cartel_radicacion():
    """Cartel Ejercicio 7"""
    print("\n-----------------------------------------------")
    print("Punto 7: función radicacion,retorna la raiz del primero respecto del segundo parámetros")
    print("----------------------------------------------")    
    print("\nRetorna la raiz del primer respecto al segundo valor")


def fun_radicacion():
    num1=int(input("ingrese el primer valor: "))
    num2=int(input("Ingrese la raiz deseada: "))
    b=1/num2
    print(pow(num1,b)) #la funcion pw me toma el primer parametro como base y el segundo la raiz
    return

if __name__ == "__main__":
    ing2i()
    ing2s()
    cartel_radicacion()
    fun_radicacion()