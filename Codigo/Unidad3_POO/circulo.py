import math

class Circulo:
    def __init__(self, radio):
        self.radio=radio

    def calculo_area(self):
        area=math.pi*pow(self.radio,2)
        return area

    def calculo_circunferencia(self):
        circ=2*math.pi*self.radio
        return circ
        

while True:
    radio = int(input("Radio del circulo: "))
    c=Circulo(radio)
    print(f"area={round(c.calculo_area(),2)}")
    print(f"circunferencia={round(c.calculo_circunferencia(),2)}")
