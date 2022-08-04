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

def cartel_potencia():
    """Cartel Ejercicio 6"""
    print("\n-----------------------------------------------")
    print("Punto 6: función potencia, , retorna la potencia del primero elevado al segundo parámetros.")
    print("----------------------------------------------")
    print("\nVamos a realizar una potencia del primer valor elevado al segundo valor")

def fun_potencia():
    numero1=float(input("Por favor ingrese el primer valor : "))
    numero2=float(input("Por favor ingrese el segundo valor: "))
    potencia=numero1**numero2
    print("Los numeros ingresados son: ",numero1," y ", numero2)
    print("la potencia entre los dos valores es: ",potencia)
    return


if __name__ == "__main__":
    ing2i()
    ing2s()
    cartel_potencia()
    fun_potencia()