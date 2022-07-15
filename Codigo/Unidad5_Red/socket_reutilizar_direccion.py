import socket
import sys


def reutilizar_direccion_socket():
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    # Obtener el estado antiguo de la opción SO_REUSEADDR
    estado_viejo = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR )
    print (f"Estado antiguo del socket: {estado_viejo}")

    # Habilitar la opción SO_REUSEADDR
    sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    estado_nuevo = sock.getsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR )
    print (f"Nuevo estado del socket: {estado_nuevo}")

    local_port = 8282
    
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind( ('', local_port) )
    srv.listen(1)
    print (f"Escuchando en el puerto: {local_port}")
    
    while True:
        try:
            connection, addr = srv.accept()
            print (f"Conectado por {addr[0]}:{addr[1]}")
        except KeyboardInterrupt:
            break
        except socket.error as msg:
            print (msg)


if __name__ == '__main__':
    reutilizar_direccion_socket()
