'''
hexlify
aton
ntoa
'''


import socket
from binascii import hexlify

def convertir_direccion_ip():
    direcciones = ['127.0.0.1', '192.168.0.1']
    
    for direccion in direcciones:
        ip_empaquetada = socket.inet_aton(direccion)
        ip_desempaquetada = socket.inet_ntoa(ip_empaquetada)
        print (f"Dirección IP: {direccion} => Empaquetada: {hexlify(ip_empaquetada)}, Desempaquetada: {ip_desempaquetada}")
   
if __name__ == '__main__':
    convertir_direccion_ip()
