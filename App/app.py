"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from Sorting import shellsort as ss

from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList() #Usando implementacion linkedlist
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

#archivo = loadCSVFile ("Data/archivosmovies/SmallMoviesDetailsCleaned.csv", sep=";")
#print (archivo['elements'][0])
#dict_keys(['elements', 'size', 'type', 'cmpfunction'])
#OrderedDict([('id', '2'), ('budget', '0'), ('genres', 'Drama|Crime'), ('imdb_id', 'tt0094675'), ('original_language', 'fi'), ('original_title', 'Ariel'), ('overview', 
#"Taisto Kasurinen is a Finnish coal miner whose father has just committed suicide and who is framed for a crime he did not commit. In jail, he starts to dream about leaving the country and starting a new life. He escapes from prison but things don't go as planned..."), ('popularity', '0.823904'), ('production_companies', 'Villealfa 
#Filmproduction Oy'), ('production_countries', 'Finland'), ('release_date', '21/10/1988'), ('revenue', '0'), ('runtime', '69'), ('spoken_languages', 'suomi'), ('status', 'Released'), ('tagline', ''), ('title', 'Ariel'), ('vote_average', '7.1'), ('vote_count', '40'), ('production_companies_number', '2'), ('production_countries_number', '1'), ('spoken_languages_number', '2')])


#Carga lista de directores con id de peliculas
#Carga lista de directores con id de peliculas
#Carga lista de directores con id de peliculas


def cargarlistadirectores (file, cmpfunction = None):
    listadirectores = lt.newList("ARRAY_LIST", cmpfunction=None)
    #print (listadirectores)
    dialect = csv.excel()
    dialect.delimiter=";"

    with open (file, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)

        for casting in row:

            
            #print (listadirectores["elements"])
            
            pos = lt.isPresent(listadirectores, casting["director_name"])
            #print (pos)
            
            
            if pos:
                director = lt.getElement(listadirectores, pos)
                lt.addFirst (director["listapeliculas"], casting["id"])
                #print (director)

            
            else:
                director = {"nombre" : None, "listapeliculas" : None}                
                director["nombre"] = casting["director_name"]                
                director["listapeliculas"] = lt.newList('SINGLE_LINKED')                
                lt.addFirst(director["listapeliculas"], casting["id"])
                
              
                lt.addLast (listadirectores, director)
                #print (listadirectores)
            
            
    
    return listadirectores





#funciones de compracion de votos:
#funciones de compracion de votos:
#funciones de compracion de votos:

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
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
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
    """
    Función para mostrar el ranking de peliculas mas votadas
    """

    ss.shellSort(lst, masvotadas)
    for contador in range(1, 11):
        pelicula = lt.getElement(lst, contador)
        print ("{}. {}, cantidad de votos: {}". format (contador, pelicula['original_title'], pelicula["vote_count"])) 

def pelismenosvotadas(lst):
    """
    Función para mostrar el ranking de peliculas menos votadas
    """

    ss.shellSort(lst, menosvotadas)
    for contador in range(1, 11):
        pelicula = lt.getElement(lst, contador)
        print ("{}. {}, cantidad de votos: {}". format (contador, pelicula['original_title'], pelicula["vote_count"])) 


def pelismejorcalificadas(lst):
    """
    Función para mostrar el ranking de peliculas mejor calificadas por su promedio de votacion
    """

    ss.shellSort(lst, mejorcalificadas)
    for contador in range(1, 11):
        pelicula = lt.getElement(lst, contador)
        print ("{}. {}, promedio de votación: {}". format (contador, pelicula['original_title'], pelicula['vote_average'])) 

def pelispeorcalificadas(lst):
    """
    Función para mostrar el ranking de peliculas con las calificaciones más bajas en su promedio de votacion
    """

    ss.shellSort(lst, peorcalificadas)
    for contador in range(1, 11):
        pelicula = lt.getElement(lst, contador)
        print ("{}. {}, cantidad de votos: {}". format (contador, pelicula['original_title'], pelicula['vote_average'])) 


#Requerimiento 3
#Requerimiento 3
#Requerimiento 3


def peliculaspordirector (listabusquedadirectores, nombrebusqueda):
    pos = lt.isPresent(listabusquedadirectores, nombrebusqueda)
    if pos:
        produccionesdirector = lt.getElement(listabusquedadirectores, pos)
        print (produccionesdirector["listapeliculas"])



#Menu principal
#Menu principal
#Menu principal



def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                listadetalles = loadCSVFile("Data/archivosmovies/SmallMoviesDetailsCleaned.csv") #llamar funcion cargar datos
                listacasting = loadCSVFile("Data/archivosmovies/MoviesCastingRaw-small.csv")
                print("Datos cargados, ",listacasting['size']," peliculas cargadas en total")
                #print(lista["elements"][3]["id"])

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
                listadedirectores = cargarlistadirectores("Data/archivosmovies/MoviesCastingRaw-small.csv")
                print (listadedirectores)

                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    #peliculaspordirector





            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()