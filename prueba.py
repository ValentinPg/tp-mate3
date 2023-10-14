import random
import requests as rq
from bs4 import BeautifulSoup
import re

#clases
class Nodo():
    
    #cuando se incializa un nodo se crea en el grafico, se le da un nombre, la url de su pagina de wikipedia y se le crea una lista con todos los links dentro de ella
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.palabras = set()
        self.parsePage(nombre)
    
    #metodo que va a fijarse si dos nodos tienen conexion, osea si uno referencia al otro
    def estaEn(self, nodo):
        if self.nombre.upper() in nodo.palabras:
            self.addEdge(nodo)
            
     
    #metodo que me creo una arista con otro nodo que le pase por parametro       
    def addEdge(self, nodo):
        pass
    
    #metodo que me crea el nodo en un grafico
    def createNode(self):
        pass
    
    #parsea con bs4 la pagina de wikipedia que le pases, obteniendo los hipervinculos dentro
    def parsePage(self,nombre):
        pass        
        #el prefijo para siguientes busquedas
        prefijo_wiki = "https://es.wikipedia.org/wiki/"
        
        url = prefijo_wiki + nombre
        #obtengo la pagina 
        page = rq.get(url)

        #la parseo en un objeto
        soup = BeautifulSoup(page.content, "html.parser")
        
        #armo una lista con los terminos que yo quiero, en este caso todos los links que refertencian a otra pagina dentro de la wikipedia
        links = soup.find_all('a', attrs={"href": re.compile("^/wiki/")},limit=200)

        #selecciono a partir de que links me va a interesar revisar (es arbitrario para reducir los link que no me importan)
        limite_inferior = 64


        #obtengo el texto y lo cargo en el set
        for i in links[limite_inferior:]:
            self.palabras.add(i.get_text().upper())
        
        #remuevo los resultados vacios
        try:
            self.palabras.remove('')
        except KeyError:
            pass
            


# creo dos nodos de prueba
mamiferos = Nodo("mamiferos")
x = Nodo("x")






# testeo, tomo una palabra random y veo cuanto tarda en accedr y parsearla 

# lista = []
# root = Nodo("mamiferos")

# while len(root.palabras) > 0:
#     nodo = Nodo(random.choice(list(root.palabras)))
#     if nodo.nombre in lista:
#         print("REPETIDO----")
#         continue
#     else:
#         lista.append(nodo.nombre)
#         print(nodo.nombre)
    


    









    
# #nodo en el centro del grafico, de el va a salir cuatro vertices 
# nodo_cetral = ["mamiferos"]

# #4 nodos que estan conectados con mamiferos
# nodos_internos = [terminos_mamiferos[1], terminos_mamiferos[2], terminos_mamiferos[7], terminos_mamiferos[18]]

# #lista con nodos totales del grafo
# nodos = nodo_cetral + nodos_internos

# #usar sets

# print(nodos)