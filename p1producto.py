from producto import fun_producto

def cartel_p1_producto():
    """Cartel Ejercicio 9"""
    print("-----------------------------------------------")
    print("Punto 9: función p1, retorna el producto de los 2 primero más el 3er parámetros,")
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
    cartel_p1_producto()
    fun_p1_producto()