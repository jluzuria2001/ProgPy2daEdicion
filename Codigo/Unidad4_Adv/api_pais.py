import urllib.request, urllib.parse
from urllib.error import HTTPError,URLError
import json
import ssl
from urllib.error import HTTPError, URLError

contexto=ssl._create_unverified_context()
url_base = 'https://restcountries.com/v3.1/name/'
pais="Spain"

def obtener_datos(pais):
    url = url_base+pais
    print(url)
    try:
        uh = urllib.request.urlopen(url, context=contexto)
    except HTTPError as e:
        print("no se ha podido recuperar nada")
    except URLError as e:
        print("no se ha podido acceder al servidor")
    else:
        data=uh.read().decode()
        print(f"Del pais {pais} se leyeron {len(data)} caracteres")
        print(type(data))
        return data

datos=obtener_datos("Spain")
diccionario=json.loads(datos)
dict=diccionario[0]
print(type(diccionario))
print(dict.keys())
print(diccionario[0]["population"])

for item, valor in dict.items():
    print(item, valor)