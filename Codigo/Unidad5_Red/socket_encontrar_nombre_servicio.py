import socket

def encontrar_nombre_servicio():
    nombre_protocolo = 'tcp'
    puertos=[80, 25]

    for puerto in puertos:
        servicio=socket.getservbyport(puerto, nombre_protocolo)
        print (f"Puerto: {puerto} => nombre del servicio: {servicio}")
    
    servicio=socket.getservbyport(53, 'udp')
    print ("Puerto: %s => nombre del servicio: {servicio}")
    
if __name__ == '__main__':
    encontrar_nombre_servicio()
