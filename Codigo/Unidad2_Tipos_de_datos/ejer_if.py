año_de_lanzamiento=1991
respuesta=input("Cuando se lanzo Python por primera vez?: ")
respuesta=int(respuesta)

if (respuesta == año_de_lanzamiento):
    print("Correcto")
elif (respuesta > año_de_lanzamiento):
    print("Demasiado alta")
elif (respuesta < año_de_lanzamiento):
    print("Demasiado bajo")
