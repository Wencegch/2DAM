from ast import If
from gettext import find
from tokenize import String

#Tenemos que realizar una aplicación, que realice el mantenimiento de una lista, cada elemento de la lista sera un diccionario 
# del registro anterior. La aplicación constara de: 
#Altas 
#Bajas 
#Modificaciones 
#Búsquedas 
#listado 

lista_articulos = []
cod_articulo = 0
nombre = ""
descripcion = ""
precio = 0
    
def alta():
        cod_articulo = input("\nCódigo artículo: ")
        nombre = input("\nNombre: ")
        descripcion = input("\nDescripción: ")
        precio = input("\nPrecio: ")
        if ( cod_articulo == 0 or nombre == "" or descripcion == "" or precio == 0):
            articulo = -1
        else:
        #Con esto se declara un diccionario
            articulo = {
                "Código artículo" : cod_articulo,
                "Nombre" : nombre,
                "Descripción" : descripcion,
                "Precio" : precio        
            }
        return articulo

def baja(cod: int):
    for i in range (len(lista_articulos)):
        if (cod == lista_articulos[i]["Código artículo"]):
            del lista_articulos[i]
        
    
def modificar(cod: int):
    res = buscar(cod)
    if (res == -1):
        print("No se puede modificar un artículo que no existe")
    else:
        
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        precio = input("Precio: ")
        
        lista_articulos[res]["Nombre"] = nombre
        lista_articulos[res]["Descripción"] = descripcion
        lista_articulos[res]["Precio"] = precio
        
def buscar(cod: int):
    for i in range (len(lista_articulos)):
        if ( cod == lista_articulos[i]["Código artículo"]):
            print(lista_articulos[i] + "\n")
            return i
    return -1

def listado():
    print(lista_articulos)
    
respuesta = ""
while (respuesta != "0"):    
    respuesta = input("1.Alta \n2.Bajas \n3.Modificaciones \n4.Busquedas \n5.Listado \n¿Qué quieres hacer?\n ")        

    if (respuesta == "1"):
        articulo = alta()
        if ( articulo != -1):
            lista_articulos.append(articulo)
    else:
        if (respuesta == "2"):
            eliminar = input("¿Qué artículo quieres dar de baja?\n")
            baja(eliminar)
        else:
            if ( respuesta == "3"):
                mod = input("Introduce el código de artículo del producto que quieras modificar\n")
                modificar(mod)
            else:
                if( respuesta == "4"):
                    find = input("¿Qué código de artículo quieres buscar?\n")
                    buscar(find)
                else:
                    if (respuesta == "5"):
                        listado()