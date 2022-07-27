def cartel_cociente():
    """Cartel Ejercicio 4"""
    print("-----------------------------------------------")
    print("Punto 4: función cociente, retorna el cociente de 2 parámetros")
    print("----------------------------------------------")
    print("\nRealizamos un cociente entre dos valores")
    
def fun_cociente(): 
    num1=float(input("Igrese el primer numero: "))
    num2=float(input("Ingrese el segundo numero: "))
    cociente=num1//num2
    print("El cociente entre el primer numero y el segundo numero es de: ",cociente)
    return

if __name__ == "__main__":
    cartel_cociente()
    fun_cociente()