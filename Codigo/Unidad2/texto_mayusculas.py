cadena=input("frase: ")

numero_caracteres=input("numero de caracteres: ")
numero_caracteres=int(numero_caracteres)

tamaño_cadena=len(cadena)
primera_parte_cadena=tamaño_cadena-numero_caracteres
texto_a_convertir=cadena[primera_parte_cadena:]

print(str(primera_parte_cadena) + str(texto_a_convertir.upper()))
