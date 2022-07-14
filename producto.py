print("Vamos a realizar un producto entre dos valores")

def producto (c,d):
    producto = c * d
    print("El resultado del producto es: ",producto)
    return producto

c=int((input("Ingresar el primer valor: ")))

d=int((input("Ingresar el segundo valor: ")))
producto(c,d)