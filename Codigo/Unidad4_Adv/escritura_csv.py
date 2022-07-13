import csv

with open('ejemplo.csv', "w", newline="") as f:
    escritor_datos=csv.writer(f)
    escritor_datos.writerow(['nombre','edad'])
    escritor_datos.writerow(['Luis','21'])

