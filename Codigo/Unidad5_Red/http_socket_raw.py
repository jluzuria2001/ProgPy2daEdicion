import socket

HTTP_REQUEST = 'GET /{path} HTTP/1.0\r\nHost: {host}\r\n\r\n'
HTTP_PUERTO = 80
BUFFER_SIZE = 1024

def parse_url(url):
    #url=http://micropython.org/ks/test.html
    #split=['micropython.org', 'ks/test.html']
    return url.replace('http://', '').split('/', 1)

def obtener_ip(host, puerto=HTTP_PUERTO):
    addr_info = socket.getaddrinfo(host, puerto)    
    # addr_info
    # [(<AddressFamily.AF_INET: 2>, 0, 0, '', 
    # ('176.58.119.26', 80))]
    print(addr_info)
    return addr_info[0][-1]

def obtener(url):
    host, path = parse_url(url)
    ip = obtener_ip(host)
    sock = socket.socket()
    sock.connect(ip)
    peticion = HTTP_REQUEST.format(host=host, path=path)
    sock.send(bytes(peticion, 'utf8'))
    respuesta = b''
    
    while True:
        trozo = sock.recv(BUFFER_SIZE)
        if not trozo:
            break
        respuesta += trozo
    
    sock.close()
    cuerpo = respuesta.split(b'\r\n\r\n', 1)[1]
    return str(cuerpo, 'utf8')


if __name__ == '__main__':
    html = obtener('http://micropython.org/ks/test.html')
    print(html)
