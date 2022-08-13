import sys
import cartel
import suma,resta,producto
import cociente,modulo,potencia,radicacion
import p1producto,p1suma,p1resta
import genrnd, genrnd_suma,genrnd_mediana,genrnd_minimo,genrnd_maximo
import genrnd2


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
            suma.ing2i()
            suma.ing2s()
            suma.cartel_suma()
            suma.fun_suma()
            sys.exit
            
        if opcion == "2":
            resta.ing2i()
            resta.ing2s()
            resta.cartel_resta()
            resta.fun_resta()
            sys.exit
            
        if opcion == "3":
            producto.ing2i()
            producto.ing2s()
            producto.cartel_producto()
            producto.fun_producto()
            sys.exit  
            
        if opcion == "4":
            cociente.ing2i()
            cociente.ing2s()
            cociente.cartel_cociente()
            cociente.fun_cociente()
            sys.exit 
            
        if opcion == "5":
            modulo.ing2i()
            modulo.ing2s()
            modulo.cartel_modulo()
            modulo.fun_modulo()
            sys.exit 
             
        if opcion == "6":
            potencia.ing2i()
            potencia.ing2s()
            potencia.cartel_potencia()
            potencia.fun_potencia()
            sys.exit
            
        if opcion == "7":
            radicacion.ing2i()
            radicacion.ing2s()
            radicacion.cartel_radicacion()
            radicacion.fun_radicacion()
            sys.exit
            
        if opcion == "9":
            p1producto.ing2i()
            p1producto.ing2s()
            p1producto.cartel_p1_producto()
            p1producto.fun_p1_producto()
            sys.exit
            
        if opcion == "10":
            p1suma.ing2i()
            p1suma.ing2s()
            p1suma.cartel_p1_suma()
            p1suma.fun_p1_suma()
            sys.exit
            
        if opcion == "11":
            p1resta.ing2i()
            p1resta.ing2s()
            p1resta.cartel_p1_resta()
            p1resta.fun_p1_resta()
            sys.exit
            
        if opcion == "12":
            genrnd.ing2i()
            genrnd.ing2s()
            genrnd.cartel_genrnd()
            genrnd.fun_genrnd()
            sys.exit
            
        if opcion == "13":
            genrnd_suma.ing2i()
            genrnd_suma.ing2s()
            genrnd_suma.cartel_genrnd_suma()
            genrnd_suma.fun_genrnd_suma()
            sys.exit
            
        if opcion == "14" or opcion == "15":
            #Cuando esta ok esta funcion hay que agregarla
            sys.exit
        
        if opcion == "16":
            #Cuando esta ok esta funcion hay que agregarla
            sys.exit
            
        if opcion == "17":
            genrnd_mediana.ing2i()
            genrnd_mediana.ing2s()
            genrnd_mediana.cartel_genrnd_mediana()
            genrnd_mediana.fun_mediana()
            sys.exit
            
        if opcion == "18":
            #Cuando esta ok esta funcion hay que agregarla
            sys.exit
        
        if opcion == "19":
            """
            falta funcion: la varianza
            """
            #Cuando esta ok esta funcion hay que agregarla
            
            sys.exit
        
        if opcion == "20":
            genrnd_minimo.ing2i()
            genrnd_minimo.ing2s()
            genrnd_minimo.cartel_genrnd_min()
            genrnd_minimo.minimo()
            sys.exit
            
        if opcion == "21":
            genrnd_maximo.ing2i()
            genrnd_maximo.ing2s()
            genrnd_maximo.cartel_genrnd_max()
            genrnd_maximo.maximo()
            sys.exit
        
        if opcion == "22":
            genrnd2.ing2i()
            genrnd2.ing2s()
            genrnd2.cartel_genrnd2()
            genrnd2.fun_genrnd2()
            sys.exit
            
        if opcion == "23":
            """
            falta funcion: Calcular la media de genrnd2
            """
            #Cuando esta ok esta funcion hay que agregarla
            sys.exit
        
        if opcion == "24":
            """
            falta funcion: Calcular la mediana de genrnd2
            """
            #Cuando esta ok esta funcion hay que agregarla
            sys.exit
        
        if opcion == "25":
            """
            falta funcion: Calcular rango de genrnd2
            """
            #Cuando esta ok esta funcion hay que agregarla
            sys.exit
        
        if opcion == "26":
            """
            falta funcion: Calcular varianza de genrnd2
            """
            #Cuando esta ok esta funcion hay que agregarla
            sys.exit
            
        if opcion == "27":
            """
            falta funcion: Calcular minimo de genrnd2
            """
            #Cuando esta ok esta funcion hay que agregarla
            sys.exit
        
        if opcion == "28":
            """
            falta funcion: Calcular maximo de genrnd2
            """
            #Cuando esta ok esta funcion hay que agregarla
            sys.exit
            
        if opcion == "29":
            """
            falta funcion: Calcular tiempo ejecucion del 16 al 21
            """
            #Cuando esta ok esta funcion hay que agregarla
            sys.exit
        
        if opcion == "30":
            """
            falta funcion: Calcular tiempo ejecucion del 22 al 28
            """
            #Cuando esta ok esta funcion hay que agregarla
            sys.exit
                        
    else:
        print("Ingrese Opcion")
        select = True
