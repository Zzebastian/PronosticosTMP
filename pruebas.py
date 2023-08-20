import requests, os, csv, re
from bs4 import BeautifulSoup
# -*- coding: utf-8 -*-
archivo = 'CVS Files/tenis.csv'
os.system('cls')

# Eliminación de Duplicados
with open(os.path.join(os.path.dirname(__file__), archivo), 'r', newline='', encoding='utf-8') as f:
    writer = csv.reader(f, delimiter=',')
    datos = list(writer)

def eliminarDuplicados(datos):
    i = 0
    while i <= len(datos)-1:
        i +=1
        if i > len(datos)-1:
            break
        a = datos[i]
        print(i)
        for j in range(i+1,len(datos)):
            if a == datos[j]:
                del datos[j]
                i -=1
            if j+1 >=len(datos):
                break

    return datos

data = eliminarDuplicados(datos)
for row in data:
    print(row)