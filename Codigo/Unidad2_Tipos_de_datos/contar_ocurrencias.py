cadena=input("Frase: ")
buscar=input("Palabra a buscar en la frase: ")

cadena=cadena.lower()
buscar=buscar.lower()

numero = cadena.count(buscar)
print (f"Hay {numero} ocurrencias de '{buscar}'")
