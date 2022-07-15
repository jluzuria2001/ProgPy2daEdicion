import socket

def probar_modos_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))
    
    socket_address = s.getsockname()
    print (f"Servidor lanzado en un socket: {str(socket_address)}")
    
    while True:
        s.listen(1)
  

if __name__ == '__main__':
    probar_modos_socket()
