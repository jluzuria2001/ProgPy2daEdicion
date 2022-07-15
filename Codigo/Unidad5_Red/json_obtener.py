'''
Ubicación actual de la Estacion Espacial (ISS) sobre la Tierra (latitud/longitud)

'''

import requests
import time

URL = 'http://api.open-notify.org/iss-now.json'

def seguimiento_estacion_espacial():
    for i in range(10):
        datos = requests.get(URL).json()     
        #{'iss_position': {'longitude': '-155.1946', 'latitude': '-4.0624'}, 
        # 'timestamp': 1637841329,
        # 'message': 'success'}
        
        posicion = datos['iss_position']     #{'longitude': '175.9980', 'latitude': '31.1778'}
        print(f"{i} lat: {posicion['latitude']} lon: {posicion['longitude']}")

        time.sleep(1)

if __name__ == '__main__':
    seguimiento_estacion_espacial()
