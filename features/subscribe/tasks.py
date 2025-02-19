from django.conf import settings
import paho.mqtt.client as mqtt
from celery import shared_task
import random


@shared_task(name="illumination_send")
def illumination_send() -> None:
    illumination = random.randint(20, 38)
    mqtt_class = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "illumination")
    mqtt_class.connect(host=settings.MQTT_BROKER_HOST, port=1883)
    mqtt_class.publish(topic="illumination", payload=illumination)
    print("illumination: " + str(illumination))


@shared_task(name="humidity_send")
def humidity_send() -> None:
    humidity = random.randint(0, 100)
    mqtt_class = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "humidity")
    mqtt_class.connect(host=settings.MQTT_BROKER_HOST, port=1883)
    mqtt_class.publish(topic="humidity", payload=humidity)
    print("humidity: " + str(humidity))


@shared_task(name="water_level_send")
def water_level_send() -> None:
    water_level = random.randint(0, 100)
    mqtt_class = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "water_level")
    mqtt_class.connect(host=settings.MQTT_BROKER_HOST, port=1883)
    mqtt_class.publish(topic="water_level", payload=water_level)
    print("water_level: " + str(water_level))


@shared_task(name="sound_send")
def sound_send() -> None:
    sound = random.randint(0, 120)
    mqtt_class = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "sound")
    mqtt_class.connect(host=settings.MQTT_BROKER_HOST, port=1883)
    mqtt_class.publish(topic="sound", payload=sound)
    print("sound: " + str(sound))
