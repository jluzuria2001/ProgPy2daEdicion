import socket
import sys
import argparse

host = 'localhost'

def cliente_eco(puerto):
    """ Un cliente de eco simple """
    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta el socket al servidor
    direccion_servidor = (host, puerto)
    print (f"Conectando a {direccion_servidor}")
    sock.connect(direccion_servidor)
    
    # Send data
    try:
        # Enviar datos
        mensaje = "Mensaje de prueba. Se hara eco de esto"
        print (f"Enviando {mensaje}")
        sock.sendall(mensaje.encode('utf-8'))
        # Busca la respuesta
        cantidad_recibida = 0
        cantidad_esperada = len(mensaje)
        
        while cantidad_recibida < cantidad_esperada:
            datos = sock.recv(16)
            cantidad_recibida += len(datos)
            print ("Recibido:", datos)
    
    except socket.error as e:
        print ("Error de socket: %s" %str(e))
    except Exception as e:
        print ("Otra excepción: %s" %str(e))
    finally:
        print ("Cerrando la conexión con el servidor")
        sock.close()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ejemplo de servidor de sockets')
    parser.add_argument('--port', action="store", dest="puerto", type=int, required=True)
    given_args = parser.parse_args() 
    puerto = given_args.puerto
    cliente_eco(puerto)


"""
python tcp_cliente_eco.py --port 60004

Conectando a ('localhost', 60004)
Enviando Mensaje de prueba. Se hara eco de esto
Recibido: b'Mensaje de prueb'
Recibido: b'a. Se hara eco d'
Recibido: b'e esto'
Cerrando la conexión con el servidor
"""
