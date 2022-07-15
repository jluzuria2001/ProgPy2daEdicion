import sys
import socket
import argparse 

def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description='Ejemplos de Errores con Sockets')
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)
    args_dados = parser.parse_args()
    
    host = args_dados.host
    port = args_dados.port
    nombre_archivo = args_dados.file
    
    # Primer bloque try-except -- crear socket 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print ("Error creating socket: %s" % e)
        sys.exit(1)
    print("1. Socket creado")

    # Segundo bloque try-except -- conecta con el host/puerto dado
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print (f"Error de dirección al conectarse al servidor: {e}")
        sys.exit(1)
    except socket.error as e:
        print ("Error de conexión: %s" % e)
        sys.exit(1)
    
    # Tercer bloque try-except -- envío de datos
    try:
        msg = "GET %s HTTP/1.0\r\n\r\n" % nombre_archivo
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print ("Error en el envío de datos: %s" % e)
        sys.exit(1)
    
    while True:
        # Cuarto bloque try-except -- esperando recibir datos del host remoto
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print ("Error en la recepción de datos: %s" % e)
            sys.exit(1)
        if not len(buf):
            break
        # escribir los datos recibidos
        sys.stdout.write(buf.decode('utf-8')) 
    
if __name__ == '__main__':
    main()
