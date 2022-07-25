class NavegadorWeb:
    conectado=True
    numero_navegadores_web=0
    geo_coordenadas={"lat":"39.466667", "lon": "-0.375"}
    
    def __init__(self, pagina):
        self.historial=[pagina]
        self.pagina_actual=pagina
        self.incognito=False
        NavegadorWeb.numero_navegadores_web+=1

    def navegar(self, nueva_pagina):
        self.pagina_actual=nueva_pagina
        if not self.incognito:
            self.historial.append(nueva_pagina)

    def limpiar_historial(self):
        self.historial[:-1]=[]

    @classmethod
    def incognito(cls, pagina):
        instancia=cls(pagina)
        instancia.incognito=True
        instancia.historial=[]
        return instancia

    @classmethod
    def cambiar_geo_coordenadas(cls, nuevas_coordenadas):
        if (int(nuevas_coordenadas["lat"])>90 or int(nuevas_coordenadas["lat"])<-90):
            print("valor no valido de la latitud")
            return None
        if (int(nuevas_coordenadas["lat"])>180 or int(nuevas_coordenadas["lat"])<-180):
            print("valor no valido de la longitud")
            return None
        cls.geo_coordenadas = nuevas_coordenadas


                

chrome=NavegadorWeb("www.as.com")
print(chrome.geo_coordenadas)
## cambiamos de ubicacion
NavegadorWeb.cambiar_geo_coordenadas({"lat":"50", "lon":"100"})
print(chrome.geo_coordenadas)
