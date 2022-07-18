"""
MONITOR
"""
from mqtt_config import *
from tabla_surf_config_estados import *
from tabla_surf_config import *
import paho.mqtt.client as mqtt
import time
import json


class TablaSurf:
    instancia_activa = None

    def __init__(self, identificador, estado, velocidad, altitud, temperatura):
        self.tabla_id = identificador
        self.estado = estado
        self.velocidad = velocidad
        self.altitud = altitud
        self.temperatura_agua = temperatura
        self.is_pubnub_connected = False
        TablaSurf.instancia_activa = self

    def construir_mensaje_json(self):
        # Construye un mensaje con el estado de la tabla de surf

        mensaje = {
            "Estado": DICCIONARIO_ESTADOS_TABLA_SURF[self.estado],
            "Velocidad (Km/h)": self.velocidad,
            "Altitud (metros)": self.altitud,
            "Temperatura agua (c)": self.temperatura_agua, 
        }
        json_mensaje = json.dumps(mensaje)
        return json_mensaje


def on_connect_mosquitto(client, userdata, flags, rc):
    print("Resultado de la conexión con Mosquitto (rc):", mqtt.connack_string(rc))
    if rc == mqtt.CONNACK_ACCEPTED:     # Comprobar si el resultado de connect es el código CONNACK_ACCEPTED
        # Suscribirse a los temas que proporcionan todos los sensores
        asunto_sensores = f"surf/{nombre_tabla_surf}/+"
        client.subscribe(asunto_sensores, qos=0)


def imprimir_mensaje_mosquitto_recibido(msg):
    print(f"Mensaje recibido. Tema: {msg.topic}. Mensaje: {str(msg.payload)}")


def on_subscribe_mosquitto(client, userdata, mid, granted_qos):
    print(f"Suscrito con QoS: {granted_qos[0]}")


def on_mensaje_mosquitto_estado(client, userdata, msg):
    imprimir_mensaje_mosquitto_recibido(msg)
    TablaSurf.instancia_activa.estado = int(msg.payload)


def on_mensaje_mosquitto_velocidad(client, userdata, msg):
    imprimir_mensaje_mosquitto_recibido(msg)
    TablaSurf.instancia_activa.velocidad = float(msg.payload)


def on_mensaje_mosquitto_altitud(client, userdata, msg):
    imprimir_mensaje_mosquitto_recibido(msg)
    TablaSurf.instancia_activa.altitud = float(msg.payload)


def on_mensaje_mosquitto_temperatura_agua(client, userdata, msg):
    imprimir_mensaje_mosquitto_recibido(msg)
    TablaSurf.instancia_activa.temperatura_agua = float(msg.payload)


def on_connect_pubnub(client, userdata, flags, rc):
    print(f"Resultado de la conexión con PubNub: {mqtt.connack_string(rc)}")
    if rc == mqtt.CONNACK_ACCEPTED:     # Comprobar si el resultado de connect es el código CONNACK_ACCEPTED
        TablaSurf.instancia_activa.is_pubnub_connected = True


def on_disconnect_pubnub(client, userdata, rc):
    TablaSurf.instancia_activa.is_pubnub_connected = False
    print("Desconectado de PubNub")


if __name__ == "__main__":

    surfboard = TablaSurf("tabla_id",1,0,0,0)

    #PUBNUB
    cliente_pubnub_id = f"{pubnub_publish_key}/{pubnub_subscribe_key}/{tabla_id}"
    cliente_pubnub = mqtt.Client(client_id=cliente_pubnub_id)
    cliente_pubnub.on_connect = on_connect_pubnub
    cliente_pubnub.on_disconnect = on_disconnect_pubnub
    cliente_pubnub.connect(host=pubnub_mqtt_server, port=pubnub_mqtt_server_port, keepalive=pubnub_mqtt_keepalive)
    cliente_pubnub.loop_start()

    #MOSQUITTO
    cliente_mosquito = mqtt.Client()
    cliente_mosquito.on_connect = on_connect_mosquitto
    cliente_mosquito.on_subscribe = on_subscribe_mosquitto
    cliente_mosquito.message_callback_add(tema_estado, on_mensaje_mosquitto_estado)
    cliente_mosquito.message_callback_add(tema_velocidad, on_mensaje_mosquitto_velocidad)
    cliente_mosquito.message_callback_add(tema_altitud, on_mensaje_mosquitto_altitud)
    cliente_mosquito.message_callback_add(tema_temperatura_agua, on_mensaje_mosquitto_temperatura_agua)
    cliente_mosquito.connect(host=mqtt_server_ip, port=mqtt_server_port, keepalive=mqtt_keepalive)
    cliente_mosquito.loop_start()

    try:
        while True:
            if TablaSurf.instancia_activa.is_pubnub_connected:
                mensaje = TablaSurf.instancia_activa.construir_mensaje_json()
                result = cliente_pubnub.publish(topic=pubnub_topic, payload=mensaje, qos=0)
                print(f"---> Publicando: {mensaje}")
            else:
                print("No conectado")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Desconectando de los servidores Mosquitto y PubNub")
        cliente_pubnub.disconnect()
        cliente_pubnub.loop_stop()
 
        cliente_mosquito.disconnect()
        cliente_mosquito.loop_stop()
