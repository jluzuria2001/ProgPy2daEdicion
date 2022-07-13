def enumerador_paquetes(paquete):
    lista_paquetes=dir(paquete)

    for elemento in lista_paquetes:
        print(elemento)

enumerador_paquetes(input("paquete?"))
