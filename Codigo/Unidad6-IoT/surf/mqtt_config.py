from tabla_surf_config import *

# Sustituir los nombres, las IPs, y las claves  
# de los host de Mosquitto y el servidor pubNub MQTT

# Local
mqtt_server_ip = "localhost"
mqtt_server_port = 1883
mqtt_keepalive = 60

# Remoto
pubnub_mqtt_server = "mqtt.pndsn.com"
pubnub_mqtt_server_port = 1883
pubnub_mqtt_keepalive = 60
pubnub_topic = nombre_tabla_surf
# Sustituir la cadena por tu clave de publicación 
# La clave de publicación suele empezar con el prefijo "pub-c-" 
pubnub_publish_key = "pub-c-ecfcf5a8-16e5-4331-9264-8e422dd6d7e9"
# Sustituir la cadena por tu clave de suscripción 
# La clave de suscripción suele empezar con el prefijo "sub-c" 
pubnub_subscribe_key = "sub-c-31a0a380-39d3-11ec-8182-fea14ba1eb2b"
