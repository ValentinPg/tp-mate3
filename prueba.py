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
terminos = list()

#obtengo el texto y lo cargo en la lista
for i in links[limite_inferior:]:
    terminos.append(i.get_text())
    
print(terminos)

#el prefijo para siguientes busquedas 
prefijo_wiki = "https://es.wikipedia.org/wiki/"
    