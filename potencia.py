def cartel_potencia():
    """Cartel Ejercicio 6"""
    print("-----------------------------------------------")
    print("Punto 6: función potencia, , retorna la potencia del primero elevado al segundo parámetros.")
    print("----------------------------------------------")
    print("\nVamos a realizar una potencia del primer valor elevado al segundo valor")

def fun_potencia():
    numero1=float(input("Por favor ingrese el primer valor : "))
    numero2=float(input("Por favor ingrese el segundo valor: "))
    potencia=numero1**numero2
    print("Los numeros ingresados son: ",numero1, numero2)
    print("la potencia entre los dos valores es: ",potencia)
    return


if __name__ == "__main__":
    cartel_potencia()
    fun_potencia()