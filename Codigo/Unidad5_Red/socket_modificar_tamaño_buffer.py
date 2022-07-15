import socket

SEND_BUF_SIZE = 2048
RECV_BUF_SIZE = 2048

def modificar_tamaño_buffer():
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    
    # Obtener el tamaño del buffer de envío del socket
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print (f"Tamaño del buffer [Antes]: {bufsize}")
    
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF, SEND_BUF_SIZE)
    sock.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_RCVBUF,
            RECV_BUF_SIZE)
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print (f"Tamaño del buffer [Despues]: {bufsize}")


if __name__ == '__main__':
    modificar_tamaño_buffer()
