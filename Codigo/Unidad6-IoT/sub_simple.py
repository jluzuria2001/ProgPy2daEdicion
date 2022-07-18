import paho.mqtt.subscribe as pub

servidor="localhost"
contenido="24 grados"
temas=["temperatura"]

mensaje_recibido=pub.simple(topics=temas, hostname=servidor)
print(f"{mensaje_recibido.topic} : {mensaje_recibido.payload}")


