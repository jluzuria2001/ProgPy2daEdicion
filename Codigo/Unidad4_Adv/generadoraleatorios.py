import random

def generador_numeros_aleatorios(numero_elementos):
    lista=[]

    for elemento in range(numero_elementos):
        lista.append(random.randint(0,1000))
    return lista


print(generador_numeros_aleatorios(int(input("cuantos numeros? "))))
