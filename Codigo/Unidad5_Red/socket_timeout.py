import socket

def probar_socket_timeout():
    print("Tiempos del timeout del socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print (f"Tiempo por defecto: {s.gettimeout()}")
    s.settimeout(100)
    print (f"Tiempo modificado a: {s.gettimeout()}")    
    
if __name__ == '__main__':
    probar_socket_timeout()
