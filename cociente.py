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
    ing2i()
    ing2s()
    cartel_cociente()
    fun_cociente()