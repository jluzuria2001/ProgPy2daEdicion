import socket
import time

HTTP_PORT = 80
TCP_BACKLOG = 0
TEMPLATE = """\
<!DOCTYPE HTML>
<html lang="en">
<head>
    <title>Servidor HTTP del Curso de Python</title>
    <meta charset="UTF-8">
    <link rel="icon" href="data:,">
    <meta name="viewport" content="width=device-width">
</head>
<body>
    <h1>Prueba con Sockets</h1>
    <b>Tiempo en funcionamiento: </b> {tiempo_en_marcha} s.
</body>
</html>
"""

def socket_escuchar():
    sock = socket.socket()
    sock.bind(('0.0.0.0', HTTP_PORT))
    sock.listen(TCP_BACKLOG)
    return sock


def servir_peticiones(sock):
    print("Servidor web iniciado")
    tiempo_inicio = time.monotonic()

    while True:
        conn, address = sock.accept()
        print('request:', address)
        request = conn.makefile('rwb')      # <_io.BufferedRWPair object at 0x00000264519E4AC0>
  
        while True:
            linea_solicitud = request.readline()
            if not linea_solicitud or linea_solicitud == b'\r\n':     #2. Uso del retorno de carro y del carácter de nueva línea
                break

        tiempo_en_marcha = time.monotonic() - tiempo_inicio
        tiempo_en_marcha=round(tiempo_en_marcha,1)
        html = TEMPLATE.format(tiempo_en_marcha=tiempo_en_marcha)
        html = bytes(html.encode())
        conn.send(html)
        conn.close()


if __name__ == '__main__':
    oyente = socket_escuchar()
    servir_peticiones(oyente)


'''
Probar:
Abrir en un navegador la dirección: 127.0.0.1:80
Observar como cambia el tiempo en ejecución del servidor
'''
