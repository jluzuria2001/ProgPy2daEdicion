import paho.mqtt.publish as pub

servidor="localhost"
contenido="24 grados"
tema="temperatura"

pub.single(topic=tema, payload=contenido, hostname=servidor)
