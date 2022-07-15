import socket
 
def obtener_info():
    nombre_equipo = socket.gethostname()
    direccion_ip = socket.gethostbyname(nombre_equipo)

    print (f"Nombre de Host: {nombre_equipo}")
    print (f"Dirección IP: {direccion_ip}")

if __name__ == '__main__':
    obtener_info()