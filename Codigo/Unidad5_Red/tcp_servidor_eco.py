import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5             # backlog especifica el número máximo de conexiones en cola


def servidor_eco(port):
    """ Un servidor de eco simple"""
    # Crear un socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Habilitar la reutilización de la dirección/puerto 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Vincular el socket al puerto
    direccion_servidor = (host, port)
    print (f"Iniciando el servidor echo en el puerto {direccion_servidor}")
    sock.bind(direccion_servidor)
    # Escuchar a los clientes
    # el argumento backlog especifica el número máximo de conexiones en cola
    sock.listen(backlog) 

    while True: 
        print ("A la espera de recibir un mensaje del cliente...")
        client, address = sock.accept() 
        datos = client.recv(data_payload) 
        
        if datos:
            print ("Datos: %s" %datos)
            client.send(datos)
            print (f"enviaron {datos} bytes de vuelta a {address}")
        # fin de la conexión
        client.close() 
   
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ejemplo de servidor de sockets')
    parser.add_argument('--port', action="store", dest="puerto", type=int, required=True)
    given_args = parser.parse_args() 
    port = given_args.puerto
    servidor_eco(port)



'''
python tcp_servidor_eco.py --port 60004
Iniciando el servidor echo en el puerto {direccion_servidor}

A la espera de recibir un mensaje del cliente...
Datos: b'Mensaje de prueba. Se hara eco de esto'
enviaron b'Mensaje de prueba. Se hara eco de esto' bytes de vuelta a ('127.0.0.1', 62889)

A la espera de recibir un mensaje del cliente...
'''