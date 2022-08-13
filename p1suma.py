from suma import fun_suma

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

def cartel_p1_suma():
    """Cartel Ejercicio 10"""
    print("\n-----------------------------------------------")
    print("Punto 10: función p1, retorna la suma de los 2 primero por el 3er parámetro")
    print("usando las funciones anteriores.")
    print("----------------------------------------------")
    print("\nRetorna la suma de los dos primeros parametros por el tercer parametro,usando las funciones anteriores")
    
    
def fun_p1_suma():
    total_suma = fun_suma()
    num3=int(input("\nIngrese el tercer valor: "))   
    fun_p1_suma=total_suma*num3
    print("El resultado total es: ",fun_p1_suma)
    return

if __name__ == "__main__":
    ing2i()
    ing2s()
    cartel_p1_suma()
    fun_p1_suma()