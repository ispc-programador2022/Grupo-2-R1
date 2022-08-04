from resta import fun_resta

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

def cartel_p1_resta():
    """Cartel Ejercicio 11"""
    print("\n-----------------------------------------------")
    print("Punto 11: función p1, retorna el producto de los 2 primero por el 3er parámetros,")
    print("usando las funciones anteriores.")
    print("----------------------------------------------")
    print("\nRetorna la resta de los dos primeros parametros por el tercer parametro,usando las funciones anteriores")
    
    
def fun_p1_resta ():
    resta= fun_resta()
    num3=int(input("Ingrese el tercer valor: "))
    funcion_p1_resta=resta*num3
    print("\nEl resultado total es: ",funcion_p1_resta)
    return funcion_p1_resta

if __name__ == "__main__":
    ing2i()
    ing2s()
    cartel_p1_resta()
    fun_p1_resta()