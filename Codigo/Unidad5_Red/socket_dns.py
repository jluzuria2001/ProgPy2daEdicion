import socket
import time

def obtener_ip(host, port=80):
    addr_info = socket.getaddrinfo(host, port)
    return addr_info[0][-1][0]


def main():
    print('realizando la búsqueda de DNS...')    
    direcciones = ['python.org', 'micropython.org', 'pypi.org']
    for direccion in direcciones:
        print(direccion, obtener_ip(direccion))


if __name__ == '__main__':
    main()
