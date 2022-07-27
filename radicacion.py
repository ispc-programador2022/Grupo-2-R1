def cartel_radicacion():
    """Cartel Ejercicio 7"""
    print("-----------------------------------------------")
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
    cartel_radicacion()
    fun_radicacion()