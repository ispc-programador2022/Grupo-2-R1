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

def cartel_producto():   
    """Cartel Ejercicio 3"""
    print("-----------------------------------------------")
    print("Punto 3: función producto, retorna el producto de 2 parámetros")
    print("----------------------------------------------")
    print("\nVamos a realizar un producto entre dos valores")

def fun_producto ():
    c=int((input("Ingresar el primer valor: ")))
    d=int((input("Ingresar el segundo valor: ")))
    producto = c * d
    print("El resultado del producto es: ",producto)
    return producto

if __name__ == "__main__":
    ing2i()
    ing2s()
    cartel_producto()
    fun_producto()