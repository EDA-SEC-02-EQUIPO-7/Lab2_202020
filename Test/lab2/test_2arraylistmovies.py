import config as cf
import sys
import csv
#from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 

import pytest 
import config 
from App import app as ap


from ADT import list as lt



def cmpfunction (element1, element2):
    if element1['elements']["id"] == element2['elements']["id"]:
        return 0
    elif element1['elements']["id"] < element2['elements']["id"]:
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


@pytest.fixture
def listamovies ():
    listamovies = ap.loadCSVFile ("Data/archivosmovies/SmallMoviesDetailsCleaned.csv")
    return listamovies


#listamovies = ap.loadCSVFile ("Data/archivosmovies/SmallMoviesDetailsCleaned.csv")
#print (listamovies.keys())
#dict_keys(['elements', 'size', 'type', 'cmpfunction'])
#print (listamovies['elements'][0])



@pytest.fixture
def lst_movies(listamovies):
    lst = lt.newList('ARRAY_LIST', cmpfunction)
    # lst = lt.newList('SINGLE_LINKED', cmpfunction)
    for i in range(len (listamovies['elements'])):    
        lt.addLast(lst,listamovies['elements'][i]) 
    return lst


def test_empty (lst):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0




def test_addFirst (lst, listamovies):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0
    lt.addFirst (lst, listamovies['elements'])
    assert lt.size(lst) == 1
    lt.addFirst (lst, listamovies['elements'])
    assert lt.size(lst) == 2
    peli = lt.firstElement(lst)
    assert peli == listamovies['elements']





def test_addLast (lst, listamovies):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0
    lt.addLast (lst, listamovies['elements'][1])
    assert lt.size(lst) == 1
    lt.addLast (lst, listamovies['elements'][2])
    assert lt.size(lst) == 2
    peli = lt.firstElement(lst)
    assert peli == listamovies['elements'][1]
    peli = lt.lastElement(lst)
    assert peli == listamovies['elements'][2]




def test_getElement(lst_movies, listamovies):
    peli = lt.getElement(lst_movies, 1)
    assert peli == listamovies['elements'][0]
    peli = lt.getElement(lst_movies, len (lst_movies['elements']))
    assert peli == listamovies['elements'][len (lst_movies['elements']) - 1]




def test_removeFirst (lst_movies, listamovies):
    assert lt.size(lst_movies) == len (lst_movies['elements'])
    lt.removeFirst(lst_movies)
    assert lt.size(lst_movies) == len (lst_movies['elements'])
    peli = lt.getElement(lst_movies, 1)
    assert peli  == listamovies['elements'][1]



def test_removeLast (lst_movies, listamovies):
    assert lt.size(lst_movies) == len (lst_movies['elements'])
    lt.removeLast(lst_movies)
    assert lt.size(lst_movies) == len (lst_movies['elements'])
    peli = lt.getElement(lst_movies, int (len (lst_movies['elements'])))
    assert peli  == listamovies['elements'][ int ((len (lst_movies['elements']) - 1))]



def test_insertElement (lst, listamovies):
    assert lt.isEmpty(lst) is True
    assert lt.size(lst) == 0
    lt.insertElement (lst, listamovies['elements'][0], 1)
    assert lt.size(lst) == 1
    lt.insertElement (lst, listamovies['elements'][1], 2)
    assert lt.size(lst) == 2
    lt.insertElement (lst, listamovies['elements'][2], 1)
    assert lt.size(lst) == 3
    peli = lt.getElement(lst, 1)
    assert peli == listamovies['elements'][2]
    peli = lt.getElement(lst, 2)
    assert peli == listamovies['elements'][0]



def test_isPresent (lst_movies, listamovies):
    peli = {('id', '2'), ('budget', '0'), ('genres', 'Drama|Crime'), ('imdb_id', 'tt0094675'), ('original_language', 'fi'), ('original_title', 'Ariel'), ('overview', "Taisto Kasurinen is a Finnish coal miner whose father has just committed suicide and who is framed for a crime he did not commit. In jail, he starts to dream about leaving the country and starting a new life. He escapes from prison but things don't go as planned..."), ('popularity', '0.823904'), ('production_companies', 'Villealfa Filmproduction Oy'), ('production_countries', 'Finland'), ('release_date', '21/10/1988'), ('revenue', '0'), ('runtime', '69'), ('spoken_languages', 'suomi'), ('status', 'Released'), ('tagline', ''), ('title', 'Ariel'), ('vote_average', '7.1'), ('vote_count', '40'), ('production_companies_number', '2'), ('production_countries_number', '1'), ('spoken_languages_number', '2')}
    #{'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    assert lt.isPresent (lst_movies, listamovies['elements'][0][0]) > 0
    assert lt.isPresent (lst_movies, peli) == 0
    


def test_deleteElement (lst_movies, listamovies):
    pos = lt.isPresent (lst_movies, listamovies['elements'][2][0])
    assert pos > 0
    peli = lt.getElement(lst_movies, pos)
    assert peli == listamovies['elements'][2]
    lt.deleteElement (lst_movies, pos)
    assert lt.size(lst_movies) == 4
    peli = lt.getElement(lst_movies, pos)
    assert peli == listamovies['elements'][3]



def test_changeInfo (lst_movies):
    book10 = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    lt.changeInfo (lst_movies, 1, book10)
    peli = lt.getElement(lst_movies, 1)
    assert book10 == peli


def test_exchange (lst_movies, listamovies):
    book1 = lt.getElement(lst_movies, 1)
    book5 = lt.getElement(lst_movies, 5)
    lt.exchange (lst_movies, 1, 5)
    assert lt.getElement(lst_movies, 1) == book5
    assert lt.getElement(lst_movies, 5) == book1