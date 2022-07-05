import sys

distancia_km=int(sys.argv[1])
tiempo_horas=int(sys.argv[2])

velocidad_kmh=distancia_km/tiempo_horas

print(velocidad_kmh)  #km/h

km_en_millas=distancia_km/1.6
metros=distancia_km*1000
segundos=tiempo_horas*3600

print("La velocidad en km/h es " + str(velocidad_kmh))
print("La velocidad en millas/h es " + str(km_en_millas/tiempo_horas))
print("La velocidad en m/s es " + str(metros/segundos))
