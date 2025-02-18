from typing import List
import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(
        self,
        broker_ip: str,
        client_name: str,
        topics: List[str],
        keepalive=60,
    ):
        self.__broker_ip = broker_ip
        self.__client_name = client_name
        self.__keepalive = keepalive
        self.__mqtt_client = None
        self.__topics = topics

    def on_connect(self, client, userdata, flags, reason_code, properties=None):
        if reason_code == 0:
            print(f"Cliente Conectado com sucesso: {client}")
            for t in self.__topics:
                client.subscribe(t)
                print(f"Subscribed to topic: {t}")
        else:
            print(f"Erro ao me conectar! codigo={reason_code}")

    def on_message(self, client, userdata, message):
        print("Mensagem recebida!")
        print(client)
        print(message.payload)

    def start_connection(self):
        mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, self.__client_name)

        mqtt_client.on_connect = self.on_connect
        mqtt_client.on_message = self.on_message

        mqtt_client.connect(host=self.__broker_ip, keepalive=self.__keepalive)
        self.__mqtt_client = mqtt_client
        self.__mqtt_client.loop_start()

    def end_connection(self):
        try:
            self.__mqtt_client.loop_stop()
            self.__mqtt_client.disconnect()
            return True
        except:
            return False
