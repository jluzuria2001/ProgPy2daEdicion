import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048

def servidor_eco(puerto):
    """ Un servidor de eco simple """
    # Crear un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Enlaza el socket con el puerto
    direccion_servidor = (host, puerto)
    print (f"Iniciando el servidor echo en {direccion_servidor}")
    sock.bind(direccion_servidor)

    while True:
        print ("Esperando a recibir mensajes del cliente")
        datos, direccion = sock.recvfrom(data_payload)
    
        print (f"recibidos {len(datos)} bytes desde {direccion}")
        print ("Datos:", datos)
    
        if datos:
            devolver = sock.sendto(datos, direccion)
            print (f"envió {devolver} bytes de vuelta a {direccion}")
            


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ejemplo de servidor de sockets')
    parser.add_argument('--port', action="store", dest="puerto", type=int, required=True)
    given_args = parser.parse_args() 
    puerto = given_args.puerto
    servidor_eco(puerto)


'''

'''