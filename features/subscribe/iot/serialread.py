import serial
import time
import ast
import schedule
import paho.mqtt.client as mqtt

def illumination_1_send(value):
    illumination_1 = value
    mqtt_class = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "illumination_1")
    mqtt_class.connect(host='mqtt.daviga.dev.br', port=1883)
    mqtt_class.publish(topic="illumination_1", payload=illumination_1)
    print("illumination_1: " + str(illumination_1))

def illumination_2_send(value):
    illumination_2 = value
    mqtt_class = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "illumination_2")
    mqtt_class.connect(host='mqtt.daviga.dev.br', port=1883)
    mqtt_class.publish(topic="illumination_2", payload=illumination_2)
    print("illumination_2: " + str(illumination_2))

def illumination_3_send(value):
    illumination_3 = value
    mqtt_class = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "illumination_3")
    mqtt_class.connect(host='mqtt.daviga.dev.br', port=1883)
    mqtt_class.publish(topic="illumination_3", payload=illumination_3)
    print("illumination_3: " + str(illumination_3))
    
def humidity_send(value):
    humidity = value
    mqtt_class = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "humidity")
    mqtt_class.connect(host='mqtt.daviga.dev.br', port=1883)
    mqtt_class.publish(topic="humidity", payload=humidity)
    print("humidity: " + str(humidity))

def temperature_send(value):
    temperature = value
    mqtt_class = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "temperature")
    mqtt_class.connect(host='mqtt.daviga.dev.br', port=1883)
    mqtt_class.publish(topic="temperature", payload=temperature)
    print("temperature: " + str(temperature))

def presence_send(value):
    presence = value
    mqtt_class = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "presence")
    mqtt_class.connect(host='mqtt.daviga.dev.br', port=1883)
    mqtt_class.publish(topic="presence", payload=presence)
    print("presence: " + str(presence))
    
def water_level_1_send(value):
    water_level_1 = value
    mqtt_class = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "water_level_1")
    mqtt_class.connect(host='mqtt.daviga.dev.br', port=1883)
    mqtt_class.publish(topic="water_level_1", payload=water_level_1)
    print("water_level_1: " + str(water_level_1))

def water_level_2_send(value):
    water_level_2 = value
    mqtt_class = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "water_level_2")
    mqtt_class.connect(host='mqtt.daviga.dev.br', port=1883)
    mqtt_class.publish(topic="water_level_2", payload=water_level_2)
    print("water_level_2: " + str(water_level_2))
    
def main_func():
    arduino = serial.Serial('COM5', 9600)
    print('Established serial connection to Arduino')
    
    try:
        arduino_data = arduino.readline(200) 
        decoded_values = arduino_data.decode("utf-8")
        print(f'Collected readings from Arduino: {decoded_values}')
        data = ast.literal_eval(decoded_values)
        print(data)

        illumination_1_send(data[0][1])
        illumination_2_send(data[1][1])
        illumination_3_send(data[2][1])

        humidity_send(data[3][1])
        temperature_send(data[4][1])

        presence_send(data[5][1])

        water_level_1_send(data[6][1])
        water_level_2_send(data[7][1])

    except UnicodeDecodeError:
        print("Erro ao decodificar. Tentando novamente...")
        return  

    arduino_data = 0
    arduino.close()
    print('<----------------------------->')

list_values = []
data = []

print('Program started')
schedule.every(5).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)