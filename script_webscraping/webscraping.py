#JUAN ANTONIO SENA CASTILLO 
#1973595
#Grupo62

import requests
import csv
from bs4 import BeautifulSoup
import datetime



#Direccion de la pagina web 
url= "http://quotes.toscrape.com/"
#Ejcuccion de Get Recuest
response= requests.get(url)
#Analizar sintacticamente el archivo HTL de BeautifulSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')
#Extraer todas las citas y autores del archivo HTML 
quotes_html = html.find_all('span', class_='text')
authors_html = html.find_all('small', class_='author')
#Crear una lisat de cittas 
quotes = list()
for quots in quotes_html:
    quotes.append(quots.text)
#Crea una lista de autores
authors = list()
for author in authors_html:
    authors.append(author.text)
#Para hacer el test: combinar y ostrar las entradas de ambas listas
for i in zip(quotes,authors):
    print(i)
#Guardar las citas y los autores en un archivo CSV en el directorio actual
#Abrir el archivo con excel libreofice, etc.

with open('./citas_1973595.csv','w') as csv_file:
    csv_writer= csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes,authors))
   
fecha_actual = datetime.datetime.now() 
# Imprimir la fecha completa (con hora y minutos)
print("Fecha y hora actual:", fecha_actual)







        



