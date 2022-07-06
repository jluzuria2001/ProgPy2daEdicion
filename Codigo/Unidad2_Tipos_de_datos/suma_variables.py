numero=5

def suma(primero, segundo):
    #logica
    total=primero+segundo+numero
    return total

def main():
    suma_por_funcion=suma(100,200)

    print(f"valor del numero: {numero}")
    print(f"el valor despues de la suma es: {suma_por_funcion}")


if __name__=="__main__":
    main()
    
