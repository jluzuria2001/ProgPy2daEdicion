import csv

with open("gente.csv", "r+", newline='') as f:
    campos=['nombre','edad']
    gente_escritor = csv.DictWriter(f, fieldnames=campos)
    gente_escritor.writeheader()
    gente_escritor.writerow({'nombre':'Jorge', 'edad':'50'})