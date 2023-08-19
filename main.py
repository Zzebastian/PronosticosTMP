import requests, os, csv, re
from bs4 import BeautifulSoup
# -*- coding: utf-8 -*-


url = 'https://www.todaymatchprediction.com/todays-tennis-predictions.html'
archivo = 'CVS Files/tenis.csv'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

print(len(soup))
tag = 'a'
Elemento = "https://www.todaymatchprediction.com/game-tips/tennis/142516887/Adrian-Mannarino-vs-Alexander-Zverev.html"
elemLinks = soup.find_all(tag,Elemento)
print(len(elemLinks))
# elem = []

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

