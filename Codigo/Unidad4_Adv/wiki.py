import requests
from bs4 import BeautifulSoup

wiki_home = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
response=requests.get(wiki_home)
#print(type(response))

def comprobar_estado(r):
	if r.status_code == 200:
		print("Exito")
		return 1
	else:
		print("Fallo")
		return -1

#print(comprobar_estado(response))


def codificacion(r):
	return (r.encoding)

codificacion(response)

def decodificar_contenido(r, codificacion):
	return (r.content.decode(codificacion))

contenido=decodificar_contenido(response, codificacion(response))
#print(type(contenido))

#len(contenido)
#print(contenido[:100])

soup = BeautifulSoup(contenido, 'html.parser')
#print(soup)

txt_dump = soup.text
#print(type(txt_dump))
#print(len(txt_dump))
#print(txt_dump[5000:5100])

idx1=txt_dump.find("Recurso del día")
#print(idx1)

idx2=txt_dump.find("Archivo")
#print(idx2)

#print(txt_dump[idx1+len("Recurso del día"):idx2])

idx3=txt_dump.find("Efemérides")
print(txt_dump[idx3+len("Efemérides"):idx3+len("Efemérides")+600])


lista_vacia=[]

for d in soup.find_all('div'): 
    if (d.get('id')=='main-itd'):
        for i in d.find_all('ul')[0]:
            #print(i.text)
            lista_vacia.append(i.text)

#print(lista_vacia)
print(lista_vacia[1])

val = "\n"
print(lista_vacia.count(val)) 

while val in lista_vacia:
    lista_vacia.remove(val)
 
print(lista_vacia)
for i in lista_vacia:
    print(i)

def wiki_en_este_dia(web):
    respuesta=requests.get(web)
    if comprobar_estado(respuesta) == 1:
        print("logica")
        contenido=decodificar_contenido(respuesta, codificacion(respuesta))
        sopa = BeautifulSoup(contenido, 'html.parser')
        texto = sopa.text
        lista_diaria=[]

        for d in soup.find_all('div'): 
            if (d.get('id')=='main-itd'):
                for i in d.find_all('ul')[0]:
                    lista_diaria.append(i.text)
        
        val = "\n"

        while val in lista_diaria:
            lista_diaria.remove(val)
 
        return lista_diaria

    else:
        print("adios")

#    return

hechos=wiki_en_este_dia(wiki_home)
for i in hechos:
    print(i)
