import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
import re


#obtengo la pagina de mamiferos
page = rq.get("https://es.wikipedia.org/wiki/mammalia")

#la parseo en un objeto
soup = BeautifulSoup(page.content, "html.parser")


#armo una lista con los terminos que yo quiero, en este caso todos los links que refertencian a otra pagina dentro de la wikipedia
links = soup.find_all('a', attrs={"href": re.compile("^/wiki/")},limit=150)

#selecciono a partir de que links me va a interesar revisar
limite_inferior = 64

#lista limpia
terminos_mamiferos = list()

#obtengo el texto y lo cargo en la lista
for i in links[limite_inferior:]:
    terminos_mamiferos.append(i.get_text())
    


#el prefijo para siguientes busquedas 
prefijo_wiki = "https://es.wikipedia.org/wiki/"
    
#nodo en el centro del grafico, de el va a salir cuatro vertices 
nodo_cetral = ["mamiferos"]

#4 nodos que estan conectados con mamiferos
nodos_internos = [terminos_mamiferos[1], terminos_mamiferos[2], terminos_mamiferos[7], terminos_mamiferos[18]]

#lista con nodos totales del grafo
nodos = nodo_cetral + nodos_internos

#usar sets

print(nodos)