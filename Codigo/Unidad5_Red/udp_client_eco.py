import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048

def cliente_eco(puerto):

    """ Un simple cliente echo """
    # Crear un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    direccion_servidor = (host, puerto)
    print ("Conectando al puerto %s %s" % direccion_servidor)
    mensaje = "Este es el mensaje de prueba. Se repetirá."

    try:
        # Enviar datos
        mensaje = "Mensaje de prueba. Se enviará de vuelta"
        print ("Enviando", mensaje)
        sent = sock.sendto(mensaje.encode('utf-8'), direccion_servidor)

        # Recibir respuesta
        datos, server = sock.recvfrom(data_payload)
        print ("recibido", datos)

    finally:
        print ("Cierre de la conexión con el servidor")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ejemplo de servidor de sockets')
    parser.add_argument('--port', action="store", dest="puerto", type=int, required=True)
    given_args = parser.parse_args() 
    puerto = given_args.puerto
    cliente_eco(puerto)
