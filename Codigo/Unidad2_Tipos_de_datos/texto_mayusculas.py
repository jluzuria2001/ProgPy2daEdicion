cadena=input("frase: ")

numero_caracteres=input("numero de caracteres: ")
numero_caracteres=int(numero_caracteres)

tamaño_cadena=len(cadena)

primera_parte_cadena=tamaño_cadena-numero_caracteres
segunda_parte_cadena=cadena[primera_parte_cadena:]

texto_a_convertir=cadena[primera_parte_cadena:]

print(cadena[:primera_parte_cadena] + str(texto_a_convertir.upper()))
