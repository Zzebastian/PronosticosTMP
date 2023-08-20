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

dia = input('Predicciones de HOY (1) o de mañana (2) \n ->')
if dia == 2:
   url = 'https://www.todaymatchprediction.com/tomorrow-tennis-predictions.html'
else:
   url = 'https://www.todaymatchprediction.com/todays-tennis-predictions.html'


# Obtención de links de encuentros
tag = 'a'
Elemento = {'class' : 'linksgogames'}
elemLinks = sopa(url, tag, Elemento)

referencias = []
for ref in elemLinks:
  rr = ref.get('href')
  referencias.append(rr)

# Obtención de predicciones sobre encuentros
tag =  'table'
Elemento = {'class' : "table table-wrap-bordered table-thead-color"}
Tabla = []
for url in referencias:
  Juego = re.split('/',url)
  Juego = Juego[6]
  Juego = Juego.replace('-', ' ')
  Juego = Juego.replace('.html', '')
  Juego = re.split(' vs ',Juego)

  tabla = sopa(url, tag, Elemento)
  tratar = str(tabla[0])
  filas = re.split('\n', tratar)
  
  prediccion = {'J1':Juego[0],
                'J2':Juego[1],
                'Gana': filas[9],
                'Gana 1º Set': filas[14],
                'Sets': filas[19],
               }
  
  for d in prediccion:
    dd = str(prediccion[d])
    dd = dd.replace('<td>', '')
    dd = dd.replace('</td>', '')
    prediccion[d] = dd
  Tabla.append(prediccion)


# Impresión de Predicciones sobre encuentros
col = 20
llaves = list(Tabla[0].keys())
print(f"{llaves[0]:<{col}} | {llaves[1]:<{col}} | {llaves[2]:<{col}} | {llaves[3]:<{col}} | {llaves[4]}")
for fila in Tabla:
  print(f"{fila[llaves[0]]:<{col}} | {fila[llaves[1]]:<{col}}  | {fila[llaves[2]]:<{col}}  | {fila[llaves[3]]:<{col}} | {fila[llaves[4]]}")


# Almacenamiento en archivos
if os.path.exists(os.path.join(os.path.dirname(__file__), archivo)):
    conf = True
else:
    os.makedirs(os.path.join(os.path.dirname(__file__), 'CVS Files/'))
    conf = False

with open(os.path.join(os.path.dirname(__file__), archivo), 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    
    if conf == False:
        writer.writerow([llaves[0], llaves[1], llaves[2], llaves[3], llaves[4]])
    
    for fila in Tabla:
        writer.writerow([fila[llaves[0]], fila[llaves[1]], fila[llaves[2]], fila[llaves[3]], fila[llaves[4]]])

# Eliminación de Duplicados
