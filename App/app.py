
import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from Sorting import mergesort as ss

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
    print("3- Consultar producciones por nombre de director")
    print("4- Consultar participaciones por actor y su principal colaboracion con un director ")
    print("5- Consultar por genero de peliculas")
    print("6- Consultar ranking por genero de películas")

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
    ss.mergesort(lst, masvotadas)
    for contador in range(1, 11):
        pelicula = lt.getElement(lst, contador)
        print ("{}. {}, cantidad de votos: {}". format (contador, pelicula['original_title'], pelicula["vote_count"]))

def pelismenosvotadas(lst):
    ss.mergesort(lst, menosvotadas)
    for contador in range(1, 11):
        pelicula = lt.getElement(lst, contador)
        print ("{}. {}, cantidad de votos: {}". format (contador, pelicula['original_title'], pelicula["vote_count"])) 

def pelismejorcalificadas(lst):
    ss.mergesort(lst, mejorcalificadas)
    for contador in range(1, 11):
        pelicula = lt.getElement(lst, contador)
        print ("{}. {}, promedio de votación: {}". format (contador, pelicula['original_title'], pelicula['vote_average'])) 

def pelispeorcalificadas(lst):
    ss.mergesort(lst, peorcalificadas)
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


def requerimiento3_lstdirector(lstcas,nombre,lstdet):
    lstdet["cmpfunction"]=cmpfunction
    if lt.isEmpty(lstcas):
        print("La lista esta vacía")  
        return 0
    else:
        
        
        lst=lt.newList("SINGLE_LINKED")
        lst["sumatoria"]=0
        iterator = it.newIterator(lstcas)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            
            if element["director_name"]==nombre:
                r=lt.isPresent(lstdet,element["id"])
                titulo=lt.getElement(lstdet,r)
                lt.addFirst(lst,titulo["original_title"])
                lst["sumatoria"]+=float(titulo["vote_average"])
                
                 
    return lst



#requerimiento4
#requerimiento4
#requerimiento4



def cmpfunction4(element1,element2):
    if element1 == element2["actor1_name"]:
        return False
    elif element1 == element2["actor2_name"]:
        return False
    elif element1 == element2["actor3_name"]:
        return False
    elif element1 == element2["actor4_name"]:
        return False
    elif element1 == element2["actor5_name"]:
        return False
    return True

def cmpfunction5(element1,element2):
    if element1 == element2["vote_average"]:
        return False
    return True

def requerimiento4(lstcas,nombre,lstdet):
    if lt.isEmpty(lstcas):
        print("La lista esta vacía")  
        return 0
    else:
        iterator = it.newIterator(lstcas)
        lst=lt.newList("SINGLE_LINKED")
        lst["sumatoria"]=0
        lst["director"]=""
        mayor=0
        directores={}
        while  it.hasNext(iterator):
            element = it.next(iterator)
            
            if cmpfunction4(nombre,element)==False:
                lstdet["cmpfunction"]=cmpfunction
                r=lt.isPresent(lstdet,element["id"])
                titulo=lt.getElement(lstdet,r)
                lt.addFirst(lst,titulo["original_title"])
                lst["sumatoria"]+=float(titulo["vote_average"])
                director=element["director_name"]
                directores[director]=directores.get(director,0)+1
                if directores[director]>mayor:
                    mayor=directores[director]
                    lst["director"]=director
            
        return lst


#requerimiento5
#requerimiento5
#requerimiento5



def cmpfunction_generos(element1,element2):
    if element1 == element2["genres"]:
        return False
    return True

def requerimiento5_generos(genero,lstdet):

    if lt.isEmpty(lstdet):
        print("La lista esta vacía")  
        return 0
    else:
        iterator = it.newIterator(lstdet)
        lst=lt.newList("SINGLE_LINKED")
        lst["sumatoria"]=0
        lst["genero"]=""
        mayor=0
        generosdict={}
        while  it.hasNext(iterator):
            element = it.next(iterator)
            
            if cmpfunction_generos(genero,element)==False:
                lstdet["cmpfunction"]=cmpfunction
                r=lt.isPresent(lstdet,element["id"])
                titulo=lt.getElement(lstdet,r)
                lt.addFirst(lst,titulo["original_title"])
                lst["sumatoria"]+=float(titulo["vote_average"])
                genero=element["genres"]
                generosdict[genero]=generosdict.get(genero,0)+1
                if generosdict[genero]>mayor:
                    mayor=generosdict[genero]
                    lst["genero"]=genero
            
        return lst



#requerimiento6
#requerimiento6
#requerimiento6


def requerimiento6_generosranking(genero,lstdet,comparatoria):
    #Funcion que recibe una lista y la ordena según la comparacion que se de como parámetro

    ss.mergesort(lstdet,comparatoria) 

    if lt.isEmpty(lstdet):
        print("La lista esta vacía")  
        return 0
    else:
        iterator = it.newIterator(lstdet)
        lst=lt.newList("ARRAY_LIST")
        lst["sumatoria"]=0
        lst["genero"]=""
        mayor=0
        generosdict={}
        while  it.hasNext(iterator):
            lstgen=lt.newList("ARRAY_LIST")

            
            #esta lista de python normal va a contener el nombre, la calificación y la cantidad de votos en ese orden. Esta es la info que se almacenará en la lista encadenada
            element = it.next(iterator)
            #print (element["id"])

            if cmpfunction_generos(genero,element)==False:
                lstdet["cmpfunction"]=cmpfunction
                r=lt.isPresent(lstdet,element["id"])
                titulo=lt.getElement(lstdet,r)
                #print (titulo.keys())

                lt.addLast(lstgen,titulo["original_title"])
                lt.addLast(lstgen,titulo["vote_average"])
                lt.addLast(lstgen,titulo["vote_count"])

                lt.addFirst(lst,lstgen)
                lst["sumatoria"]+=float(titulo["vote_average"])
                
                genero=element["genres"]
                generosdict[genero]=generosdict.get(genero,0)+1
                if generosdict[genero]>mayor:
                    mayor=generosdict[genero]
                    lst["genero"]=genero
       
            
        return lst
         

#main
#main
#main
            
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

                



            elif int(inputs[0])==2: #opcion 2 ranking mejores/peores peliculas - Requerimiento 2
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



            elif int(inputs[0])==3: #Requerimiento 3 - conocer peliculas de un director
                if listadetalles==None or listadetalles['size']==0: #consultar_pelis_director
                    print("lista vacia")
                else:
                    director=input("Escriba un director ")
                    directores=requerimiento3_lstdirector(listacasting,director,listadetalles)
                    if directores["size"]==0:
                        print("Ese actor no existe")
                    else:
                        
                        print("Ha participado en "+str(directores["size"])+" peliculas" )
                        print("El promedio de calificación de sus peliculas es: "+ str(round(directores["sumatoria"]/int(directores["size"]))))
                        print("Las peliculas en las que ha estado son:")
                        iterator = it.newIterator(directores)
                        while  it.hasNext(iterator):
                            element = it.next(iterator)
                            print(element)


            elif int(inputs[0])==4: #Requerimiento 4 - consultar por actor, sus apariciones y colaboracioes con director
                if listadetalles==None or listadetalles['size']==0: 
                    print("lista vacia")
                else:
                    nombre=input("Escriba un actor")        
                    r4=requerimiento4(listacasting,nombre,listadetalles)
                    if r4["size"]==0:
                        print("Ese actor no existe")
                    else:
                        print("El director con el que más ha trabajado es:"+ r4["director"])
                        print("Ha participado en "+str(r4["size"])+" peliculas" )
                        print("El promedio de calificación de sus peliculas es: "+ str(round(r4["sumatoria"]/int(r4["size"]))))
                        print("Las peliculas en las que ha estado son:")
                        iterator = it.newIterator(r4)
                        while  it.hasNext(iterator):
                            element = it.next(iterator)
                            print(element)

            elif int(inputs[0])==5: #Requerimiento 5 - conocer peliculas por genero, con su respectiva calificacion
                if listadetalles==None or listadetalles['size']==0: 
                    print("lista vacia")
                else:
                    genero_busqueda=input("Escriba un genero de películas que desee consultar:\n")        
                    listageneros = requerimiento5_generos(genero_busqueda,listadetalles)
                    
                    
                    if listageneros["size"]==0:
                        print("El género ingresado no tiene coincidencias en nuestro registro")
                    else:
                        print("\nPara el género {}, se encontraron en total {} películas:\n" .format(genero_busqueda, str(listageneros["size"])))
                        iterator = it.newIterator(listageneros)
                        
                        while  it.hasNext(iterator):
                            element = it.next(iterator)
                            print("->" + element)

                        print ("\nEl promedio de calificación obtenido en estas películas es: "+ str(round( (listageneros["sumatoria"]/int(listageneros["size"])),2  )))



            elif int(inputs[0])==6: #Requerimiento 6 - rankings por genero 
                if listadetalles==None or listadetalles['size']==0: 
                    print("lista vacia")
                else:
                    palabra = ""
                    observacion = ""
                    print ("En esta opcíon puede consultar el mejor y el peor ranking de las peliculas por género:")
                    generoranking=input("Escriba un genero de consulta:\n")
                    
                    comparacionseleccionada = input ("Escriba \"A\" si desea consultar por cantidad de votos o \"B\" si desea consultar por calificacion:\n")

                    if comparacionseleccionada == "A":
                        #es contraintuitivo que low este con la funcion de masvotadas, pero así funciona, entonces no la cambiemos. Igual en B
                        generoslow=requerimiento6_generosranking(generoranking,listadetalles,masvotadas)
                        generostop=requerimiento6_generosranking(generoranking,listadetalles,menosvotadas)
                        palabra = "votaciones en total"
                        observacion = 2
                    
                    elif comparacionseleccionada == "B":
                        generoslow=requerimiento6_generosranking(generoranking,listadetalles,mejorcalificadas)
                        generostop=requerimiento6_generosranking(generoranking,listadetalles,peorcalificadas)
                        palabra = "de calificación"
                        observacion = 1

                    else:
                        print("opción no válida")

                    if generoslow["size"]==0:
                        print("El género ingresado no tiene coincidencias en nuestro registro")
                    else:
                        print("\nPara el género {}, se encontraron en total {} películas:\n" .format(generoranking, str(generoslow["size"])))
                        
                        iterator = it.newIterator(generostop)
                        element = it.next(iterator)
                        #print (element)
                        print ("Las 10 mejores peliculas son:\n")
                        sumatoriatop = 0
                        for i in range (10):
                            print (str(i+1) + ". " + lt.getElement(element,0)+ ", con " + str ( element["elements"][2])+ " votos, cuyo promedio es "+element["elements"][1])
                            element = it.next(iterator) 
                            sumatoriatop+=float(element["elements"][1])
                        promediotop = round ((sumatoriatop/10),2)
                        print ("\nEl promedio de " + palabra +" para estas películas es de: " + str(promediotop))
                        iterator = it.newIterator(generoslow)
                        element = it.next(iterator)
                        sumatoriatop = 0
                        print ("\n\nLas 10 peores peliculas son:\n")
                        for i in range (10):
                            print (str(i+1) + ". " + element["elements"][0]+ ", con " + str ( element["elements"][2])+ " votos, cuyo promedio es "+element["elements"][1])
                            element = it.next(iterator)
                            sumatoriatop+=float(element["elements"][1])
                        promediotop = round ((sumatoriatop/10),2)
                        print ("\nEl promedio de " + palabra +" para estas películas es de: " + str(promediotop))   
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()
