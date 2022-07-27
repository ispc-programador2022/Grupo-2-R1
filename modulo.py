def cartel_modulo():
    """Cartel Ejercicio 5"""
    print("-----------------------------------------------")
    print("Punto 5: función modulo, retorna el modulo de 2 parámetros")
    print("----------------------------------------------")
    print("\nRealizamos el modulo entre dos numeros")
    
def fun_modulo():
    num1=int(input("Igrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    modulo=num1%num2
    print("Los valores ingresados son: ",num1,num2)
    print("El Modulo entre el primer numero y el segundo numero es de: ",modulo)
    return

if __name__ == "__main__":
    cartel_modulo()
    fun_modulo()