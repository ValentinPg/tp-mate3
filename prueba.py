import random
import requests as rq
from bs4 import BeautifulSoup
import re
import networkx as nx

#clases
class Nodo():
    
    #cuando se incializa un nodo se crea en el grafico, se le da un nombre, la url de su pagina de wikipedia y se le crea una lista con todos los links dentro de ella
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.palabras = set()
        self.parsePage(nombre)
    
    #metodo que va a fijarse si dos nodos tienen conexion, osea si uno referencia al otro
    def estaEn(self, nodo):
        if self.nombre.lower() in nodo.palabras:
            self.addEdge(nodo)
            
     
    #metodo que me creo una arista con otro nodo que le pase por parametro       
    def addEdge(self, nodo):
        return (self.nombre, nodo.nombre)
    
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
        links = soup.find_all('a', attrs={"href": re.compile("^/wiki/")})

        print(links)

        #selecciono a partir de que links me va a interesar revisar (es arbitrario para reducir los link que no me importan)
        limite_inferior = 0


        #obtengo el texto y lo cargo en el set
        for i in links[limite_inferior:]:
            self.palabras.add(i.get_text().lower().replace(" ","_"))
            
        
        #remuevo los resultados vacios
        try:
            self.palabras.remove('')
        except KeyError:
            pass
        
        try:
            self.palabras.remove("limitación_de_responsabilidad")
        except KeyError:
            pass
        
        try:
            self.palabras.remove("acerca_de_wikipedia")
        except KeyError:
            pass
        
            


# # creo dos nodos de prueba
# # mamiferos = Nodo("mamiferos")
# # x = Nodo("x")

# #lista que va a tener todos los nodos del grafico
# nodos = list()
# # lista que contiene los vertices
# vertices = list()

# #nodo central
# nodo_maestro = Nodo("mamiferos")
# # lo agrego a la lista con todos los nodos
# nodos.append(nodo_maestro)


# # obtengo un nodo aleatorio
# nodo = Nodo(list(nodo_maestro.palabras)[random.randrange(0,len(nodo_maestro.palabras))])
# nodo_anterior = nodo_maestro

# for i in range(10):
#     print(nodo.nombre)
#     if (len(nodo.palabras)>0):
#         vertices.append((nodo_anterior.nombre, nodo.nombre))
#         nodo_anterior = nodo
#         nodos.append(nodo)
#         nodo = Nodo(list(nodo.palabras)[random.randrange(0,len(nodo.palabras))]) # cambiar nodo_maestro por nodo
#     else:
#         nodo =  Nodo(random.choice(list(nodo_anterior.palabras)))

# for i in nodos:
#     print(i.nombre)
    


# for i in nodos:
#     for j in nodos:
#         t = i.estaEn(j)
#         if t != None:
#             vertices.append(t)
        
# print(vertices)



# grafo = nx.Graph()

# grafo.add_nodes_from(nodos)
# grafo.add_edges_from(vertices)
# nx.draw(grafo)

Nodo("mamiferos")