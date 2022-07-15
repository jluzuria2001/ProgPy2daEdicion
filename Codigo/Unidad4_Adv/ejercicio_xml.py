import xml
import xml.etree.ElementTree as ET

datos='''
<persona>
    <nombre>Juan</nombre>
    <apellido>Perez</apellido>
    <telefono tipo="movil">601814456</telefono>
    <correoe trabajo="si">juan.p@gmail.com</correoe>
</persona>
'''
arbol = ET.fromstring(datos)

#print(datos)
#print(arbol)    # posicion de memoria donde esta el arbol

print(arbol.find("nombre").text)
print(arbol.find("telefono").get('tipo'))