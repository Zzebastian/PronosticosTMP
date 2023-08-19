import requests, os, csv, re
from bs4 import BeautifulSoup
# -*- coding: utf-8 -*-
archivo = 'CVS Files/tenis.csv'

def sopa(url, tag, Elemento):
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  elemLinks = soup.find_all(tag,Elemento)
  return elemLinks
#

url = 'https://www.todaymatchprediction.com/todays-tennis-predictions.html'
tag = 'a'
Elemento = {'class' : 'linksgogames'}
elemLinks = sopa(url, tag, Elemento)


referencias = []
for ref in elemLinks:
  rr = ref.get('href')
  referencias.append(rr)
#print(referencias)

url = referencias[0]
tag =  'table'
Elemento = {'class' : "table table-wrap-bordered table-thead-color"}
tabla = sopa(url, tag, Elemento)
print(len(tabla))

tratar = str(tabla[0])
filas = re.split('\n', tratar)
print(len(filas))
i = 0
# for EEE in filas:
#   print(i, EEE)
#   i+=1
for II in (8,9,13,14,18,19):
  print(filas[II])
# print(filas)
# for link in elemLinks:
#     elem.append(link.text)

# if os.path.exists(os.path.join(os.path.dirname(__file__), archivo)):
#     conf = True
# else:
#     os.makedirs(os.path.join(os.path.dirname(__file__), 'CVS Files/'))
#     conf = False



# with open(os.path.join(os.path.dirname(__file__), archivo), 'a', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter=',')
    
#     if conf == False:
#         writer.writerow(['Equipo 1', 'Equipo 2', 'Ganador', 'Probabilidad', 'Fecha'])
    
#     for partido in encuentros:
#         writer.writerow([partido['Equipo1'], partido['Equipo2'], partido['Ganador'], partido['Probabilidad'], partido["Fecha"]])

