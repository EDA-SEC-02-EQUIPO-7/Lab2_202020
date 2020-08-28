
import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from Sorting import shellsort as ss

from time import process_time 

def cmpfunction(element1,element2):
    if element1 == element2["id"]:
        return False
    return True
def loadCSVFile (file, sep=";"):
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList("SINGLE_LINKED") #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                #print (row)
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de las 10 mejores y las 10 peores peliculas")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Consultar elementos a partir de dos listas")
    print("6- Consultar peliculas de un director")
    print("7- Consultar elementos a partir de dos listas")
    print("8- Consultar elementos a partir de dos listas")
    print("9- Consultar elementos a partir de dos listas")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    
    """

    return 0

#Requerimiento2
#Requerimiento2
#Requerimiento2

def pelismasvotadas(lst):
    ss.shellSort(lst, masvotadas)
    for contador in range(1, 11):
        pelicula = lt.getElement(lst, contador)
        print ("{}. {}, cantidad de votos: {}". format (contador, pelicula['original_title'], pelicula["vote_count"])) 
def pelismenosvotadas(lst):
    ss.shellSort(lst, menosvotadas)
    for contador in range(1, 11):
        pelicula = lt.getElement(lst, contador)
        print ("{}. {}, cantidad de votos: {}". format (contador, pelicula['original_title'], pelicula["vote_count"])) 
def pelismejorcalificadas(lst):
    ss.shellSort(lst, mejorcalificadas)
    for contador in range(1, 11):
        pelicula = lt.getElement(lst, contador)
        print ("{}. {}, promedio de votación: {}". format (contador, pelicula['original_title'], pelicula['vote_average'])) 
def pelispeorcalificadas(lst):
    ss.shellSort(lst, peorcalificadas)
    for contador in range(1, 11):
        pelicula = lt.getElement(lst, contador)
        print ("{}. {}, cantidad de votos: {}". format (contador, pelicula['original_title'], pelicula['vote_average'])) 
def peliculaspordirector (listabusquedadirectores, nombrebusqueda):
    pos = lt.isPresent(listabusquedadirectores, nombrebusqueda)
    if pos:
        produccionesdirector = lt.getElement(listabusquedadirectores, pos)
        print (produccionesdirector["listapeliculas"])
def masvotadas (peli1, peli2):
    if int (peli1['vote_count']) > int (peli2['vote_count']):
        return True
    return False
def menosvotadas (peli1, peli2):
    if int (peli1['vote_count']) < int (peli2['vote_count']):
        return True
    return False
def mejorcalificadas (peli1, peli2):
    if float (peli1['vote_average']) > float (peli2['vote_average']):
        return True
    return False

def peorcalificadas (peli1, peli2):
    if float (peli1['vote_average']) < float (peli2['vote_average']):
        return True
    return False
#requerimiento3
#requerimiento3
#requerimiento3

def cmpfunction3 (element1, element2):
    if element1 == element2["nombre"]:
        return False
    return True
def requerimiento3_lstdirector(lstcas,nombre,lstdet):
    lstdet["cmpfunction"]=cmpfunction
    if lt.isEmpty(lstcas):
        print("La lista esta vacía")  
        return 0
    else:
        lst = lt.newList("SINGLE_LINKED",cmpfunction3)
        iterator = it.newIterator(lstcas)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if element["director_name"]==nombre:
                r=lt.isPresent(lstdet,element["id"])
                titulo=lt.getElement(lstdet,r)
                print(titulo["original_title"]) 
                 
    return lst

#requerimiento4
#requerimiento4
#requerimiento4

def main():
    lista = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                listadetalles = loadCSVFile("Data\SmallMoviesDetailsCleaned.csv") #llamar funcion cargar datos
                listacasting = loadCSVFile("Data\MoviesCastingRaw-small.csv")
                
                print("Datos cargados, ",listacasting['size']," peliculas cargadas en total")
            elif int(inputs[0])==2: #opcion 2
                if listacasting==None or listacasting['size']==0 or listadetalles==None or listadetalles['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: 
                    print("La lista tiene ",listacasting['size']," elementos")
                    print ("Con esta opción ud puede escoger entre ver el ranking según la cantidad de votos o el promedio de votación")
                    print ("A - Ranking por cantidad de votos")
                    print ("B - Ranking por promedio de votación")
                    seleccion = input ("Ingrese la letra que define la opcion que desea:\n")
                    if seleccion == "A":
                        print ("\nLas peliculas con mayor cantidad de votos son: ")
                        pelismasvotadas(listadetalles)
                        print ("\nLas peliculas con menor cantidad de votos son: ")
                        pelismenosvotadas(listadetalles)
                        
                    elif seleccion == "B":
                        print ("\nLas peliculas con mayor calificación son: ")
                        pelismejorcalificadas(listadetalles)
                        print ("\nLas peliculas con menor calificación son: ")
                        pelispeorcalificadas(listadetalles)
                    else:
                        print ("\nLa letra escogida no corresponde a ninguna opción!")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==6: #opcion 6
                if listadetalles==None or listadetalles['size']==0: #consultar_pelis_director
                    print("lista vacia")
                else:
                    director=input("Escriba un director ")
                    directores=requerimiento3_lstdirector(listacasting,director,listadetalles)
                    
                    
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()
