class Ascensor:
    capacidad_maxima = 8

    def __init__(self, ocupantes):
        
        if (ocupantes > self.capacidad_maxima):
            print(f"Se excede la capacidad del ascensor {ocupantes-self.capacidad_maxima} deben salir")
        self.ocupantes=ocupantes


##ascensor1=Ascensor(6)
##print(f"Ascensor1 tiene {ascensor1.ocupantes}")

ascensor2=Ascensor(10)
print(f"Ascensor2 tiene {ascensor2.ocupantes}")
