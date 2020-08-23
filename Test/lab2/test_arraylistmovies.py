"""
import pytest 
import config 
from DataStructures import arraylist as slt


def loadCSVFile (file, sep=";"):
    # ""
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
    #""
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
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst

    """

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 

import pytest 
import config 
from App import app as ap


from ADT import list as lt



def cmpfunction (element1, element2):
    if element1['id'] == element2['id']:
        return 0
    elif element1['id'] < element2['id']:
        return -1
    else:
        return 1


@pytest.fixture
def lst ():
    # lst = lt.newList('SINGLE_LINKED', cmpfunction)
    lst = lt.newList('ARRAY_LIST', cmpfunction)
    return lst


@pytest.fixture
def books ():
    books = []
    books.append({'book_id':'1', 'book_title':'Title 1', 'author':'author 1'})
    books.append({'book_id':'2', 'book_title':'Title 2', 'author':'author 2'})
    books.append({'book_id':'3', 'book_title':'Title 3', 'author':'author 3'})
    books.append({'book_id':'4', 'book_title':'Title 4', 'author':'author 4'})
    books.append({'book_id':'5', 'book_title':'Title 5', 'author':'author 5'})
    print (books[0])
    return books


listamovies = ap.loadCSVFile ("Data/archivosmovies/SmallMoviesDetailsCleaned.csv")
print (listamovies)



@pytest.fixture
def lstmovies(listamovies):
    lst = lt.newList('ARRAY_LIST', cmpfunction)
    # lst = lt.newList('SINGLE_LINKED', cmpfunction)
    for i in range(len (listamovies)):    
        lt.addLast(lst,listamovies[i])    
    return lst


def test_empty (lst):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0




def test_addFirst (lst, listamovies):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0
    lt.addFirst (lst, listamovies[1])
    assert lt.size(lst) == 1
    lt.addFirst (lst, listamovies[2])
    assert lt.size(lst) == 2
    peli = lt.firstElement(lst)
    assert peli == listamovies[2]





def test_addLast (lst, listamovies):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0
    lt.addLast (lst, listamovies[1])
    assert lt.size(lst) == 1
    lt.addLast (lst, listamovies[2])
    assert lt.size(lst) == 2
    peli = lt.firstElement(lst)
    assert peli == listamovies[1]
    peli = lt.lastElement(lst)
    assert peli == listamovies[2]




def test_getElement(lstmovies, listamovies):
    peli = lt.getElement(lstmovies, 1)
    assert peli == listamovies[0]
    peli = lt.getElement(lstmovies, 5)
    assert peli == listamovies[4]




def test_removeFirst (lstmovies, listamovies):
    assert lt.size(lstmovies) == 5
    lt.removeFirst(lstmovies)
    assert lt.size(lstmovies) == 4
    peli = lt.getElement(lstmovies, 1)
    assert peli  == listamovies[1]



def test_removeLast (lstmovies, listamovies):
    assert lt.size(lstmovies) == 5
    lt.removeLast(lstmovies)
    assert lt.size(lstmovies) == 4
    peli = lt.getElement(lstmovies, 4)
    assert peli  == listamovies[3]



def test_insertElement (lst, listamovies):
    assert lt.isEmpty(lst) is True
    assert lt.size(lst) == 0
    lt.insertElement (lst, listamovies[0], 1)
    assert lt.size(lst) == 1
    lt.insertElement (lst, listamovies[1], 2)
    assert lt.size(lst) == 2
    lt.insertElement (lst, listamovies[2], 1)
    assert lt.size(lst) == 3
    peli = lt.getElement(lst, 1)
    assert peli == listamovies[2]
    peli = lt.getElement(lst, 2)
    assert peli == listamovies[0]



def test_isPresent (lstmovies, listamovies):
    peli = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    assert lt.isPresent (lstmovies, listamovies[2]) > 0
    assert lt.isPresent (lstmovies, peli) == 0
    


def test_deleteElement (lstmovies, listamovies):
    pos = lt.isPresent (lstmovies, listamovies[2])
    assert pos > 0
    peli = lt.getElement(lstmovies, pos)
    assert peli == listamovies[2]
    lt.deleteElement (lstmovies, pos)
    assert lt.size(lstmovies) == 4
    peli = lt.getElement(lstmovies, pos)
    assert peli == listamovies[3]



def test_changeInfo (lstmovies):
    book10 = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    lt.changeInfo (lstmovies, 1, book10)
    peli = lt.getElement(lstmovies, 1)
    assert book10 == peli


def test_exchange (lstmovies, listamovies):
    book1 = lt.getElement(lstmovies, 1)
    book5 = lt.getElement(lstmovies, 5)
    lt.exchange (lstmovies, 1, 5)
    assert lt.getElement(lstmovies, 1) == book5
    assert lt.getElement(lstmovies, 5) == book1