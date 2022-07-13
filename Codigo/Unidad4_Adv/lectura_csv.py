import csv

filepath="c:\\Users\\jluzuriaga\\Documents\\cursoPython2ed\\Unidad4\\MOCK_DATA.csv"
with open(filepath, 'r') as f:
           
    lector_datos=csv.reader(f)
    contador_linea=1

    for fila in lector_datos:
        if contador_linea > 1:
            print(fila)
        contador_linea+=1