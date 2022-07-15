import os
import xml
import xml.etree.ElementTree as ET

filepath=(f"{os.getcwd()}\\xml_ej2.xml")
arbol = ET.parse(filepath)
#print(arbol)
padre=arbol.getroot()
print(padre)

for hijo in padre:
    print(hijo.tag, hijo.attrib)

print("-"*20)
pib=padre[0][2].text
print(f"el pib {pib}")
print(padre[0].attrib['nombre'])

print("-"*20)

for item in padre:
    pais=item.attrib['nombre']
    pib=item[2].text
    print(pais, pib)
