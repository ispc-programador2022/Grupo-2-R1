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

def cartel_modulo():
    """Cartel Ejercicio 5"""
    print("-----------------------------------------------")
    print("Punto 5: función modulo, retorna el modulo de 2 parámetros")
    print("----------------------------------------------")
    print("\nRealizamos el modulo entre dos numeros")
    
def fun_modulo():
    num1=int(input("Igrese el 1er num: "))
    num2=int(input("Ingrese el 2do num: "))
    modulo=num1%num2
    print("Los valores ingresados son: ",num1," y ",num2)
    print("El Modulo entre el primer numero y el segundo numero es de: ",modulo)
    return

if __name__ == "__main__":
    ing2i()
    ing2s()
    cartel_modulo()
    fun_modulo()