from producto import fun_producto

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

def cartel_p1_producto():
    """Cartel Ejercicio 9"""
    print("-----------------------------------------------")
    print("Punto 9: función p1, retorna el producto de los 2 primero por el 3er parámetros,")
    print("usando las funciones anteriores.")
    print("----------------------------------------------")
    print("\nRetorna el producto de los dos primeros parametros mas el tercer parametro,usando las funciones anteriores")
    
    
def fun_p1_producto():
    total_producto = fun_producto()
    num3=int(input("Ingrese el tercer valor: "))   
    fun_p1_producto=total_producto+num3
    print("El resultado total es: ",fun_p1_producto)
    return

if __name__ == "__main__":
    ing2i()
    ing2s()
    cartel_p1_producto()
    fun_p1_producto()