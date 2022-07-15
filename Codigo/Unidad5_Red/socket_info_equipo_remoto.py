import socket

def obtener_info():
    nombre_equipo = 'www.python.org'
    direccion_ip = socket.gethostbyname(nombre_equipo)

    try:
        print(f"Dirección IP de {nombre_equipo} es {direccion_ip}")
    except socket.error as err_msg:
        print(f"{nombre_equipo}, {err_msg}")
    
if __name__ == '__main__':
    obtener_info()
