import requests
from bs4 import BeautifulSoup

URL = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
respuesta = requests.get(URL)

#print(response)
print(type(respuesta))

#1
def comprobar_estado(respuesta):
    if respuesta.status_code == 200:
        print ("bien")
        return 1
    else:
        print ("mal")
        return -1

comprobar_estado(respuesta)

#2
def codificacion(r):
    return(r.encoding)

print(codificacion(respuesta))

# fun decodicar
def decodificar(r, codificacion):
    return r.content.decode(codificacion)

contenido=decodificar(respuesta, codificacion(respuesta))

# el tratamiento
sopa=BeautifulSoup(contenido, 'html.parser')

#print(type(contenido))

texto=sopa.text
#print(texto)

idx1=texto.find("Recurso del día")
idx2=texto.find("Archivo")

#print(texto[idx1:idx2])

## 2da forma


lista_vacia=[]

for d in sopa.find_all('div'):
    if (d.get('id') == 'main-itd'):
        for i in d.find_all('ul')[0]:
            lista_vacia.append(i.text)


val = "\n"
print(lista_vacia.count(val)) 

while val in lista_vacia:
    lista_vacia.remove(val)
 
print(lista_vacia)

for i in lista_vacia:
    print(i)