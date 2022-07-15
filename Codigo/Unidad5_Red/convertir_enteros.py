import socket

def convertir_enteros():
    data = 1234
    host_byte_32=socket.ntohl(data)
    red_byte_32=socket.htonl(data)
    host_byte_16=socket.ntohs(data)
    red_byte_16=socket.htons(data)

    # 16-bit
    print("Valores cortos de orden de bytes")
    print (f"Original: {data} => del host: {host_byte_16}, de la red: {red_byte_16}")
    
    # 32-bit
    print("Valores largos de orden de bytes")
    print (f"Original: {data} => del host: {host_byte_32}, de la red: {red_byte_32}")
    
if __name__ == '__main__':
    convertir_enteros()
    