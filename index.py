import sys
import cartel
import suma,resta,producto
import cociente,modulo,potencia,radicacion
import p1producto

class Main:
    """
    Clase que se encarga de administrar
    y lanza las funciones
    """
    
    def __init__(self):
        cartel.cartel_index()
        cartel.cartel_menu()
                        
            
if __name__ == "__main__":
    principal = Main()
    select = True
    while select:
            
        opcion = input("\nIngrese Opcion Menu : ")
        if opcion == "0":
            cartel.cartel_menu()
            sys.exit
        if opcion == "00":
            cartel.cartel_menu_dos()
            sys.exit
        if opcion == "000":
            cartel.cartel_menu_tres()
            sys.exit
        if opcion == "1":
            suma.cartel_suma()
            suma.fun_suma()
            sys.exit
        if opcion == "2":
            resta.cartel_resta()
            resta.fun_resta()
            sys.exit
        if opcion == "3":
            producto.cartel_producto()
            producto.fun_producto()
            sys.exit  
        if opcion == "4":
            cociente.cartel_cociente()
            cociente.fun_cociente()
            sys.exit 
        if opcion == "5":
            modulo.cartel_modulo()
            modulo.fun_modulo()
            sys.exit  
        if opcion == "6":
            potencia.cartel_potencia()
            potencia.fun_potencia()
            sys.exit
        if opcion == "7":
            radicacion.cartel_radicacion()
            radicacion.fun_radicacion()
            sys.exit
        if opcion == "9":
            p1producto.cartel_p1_producto()
            p1producto.fun_p1_producto()
            sys.exit
        if opcion == "10":
            """
            si te animas coloca aca los archivos,
            recordar importarlos primero
            arriba 
            """
            #primero funcion cartel_funcion() p1 suma
            #funcion p1 suma
            sys.exit
        if opcion == "11":
            #aca iria el cartel de p1 resta
            #aca la funcion p1 resta
            sys.exit
                        
    else:
        print("Ingrese Opcion")
        select = True
