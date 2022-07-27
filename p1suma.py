from suma import suma

def cartel_p1_suma():
    """Cartel Ejercicio 9"""
    print("-----------------------------------------------")
    print("Punto 9: función p1, retorna la suma de los 2 primero por el 3er parámetros,")
    print("usando las funciones anteriores.")
    print("----------------------------------------------")
    print("\nRetorna la suma de los dos primeros parametros por el tercer parametro,usando las funciones anteriores")
    
    
def fun_p1_suma():
    total_suma = suma()
    num3=int(input("Ingrese el tercer valor: "))   
    fun_p1_suma=total_suma+num3
    print("El resultado total es: ",fun_p1_suma)
    return

if __name__ == "__main__":
    cartel_p1_suma()
    fun_p1_suma()



	
