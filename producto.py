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
    cartel_producto()
    fun_producto()