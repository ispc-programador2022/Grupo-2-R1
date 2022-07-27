def cartel_suma():
    """Cartel Ejercicio 1"""
    print("-----------------------------------------------")
    print("Punto 1: función suma, retorna la suma de 2 parámetros")
    print("----------------------------------------------")
    print("  ")
    
def fun_suma():
    a=int((input("Ingresar el primer valor: ")))
    b=int((input("Ingresar el segundo valor: ")))
    suma = a + b
    print("El resultado de la suma es: ",suma)
    return suma

if __name__ == "__main__":
    cartel_suma()
    fun_suma()