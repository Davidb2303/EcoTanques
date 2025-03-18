import paho.mqtt.client as mqtt
import json
from django.utils.timezone import now
from Tanks.Tank.models import Tanque
from Tanks.SensorData.models import Sensor
from Tanks.Medition.models import Medicion

# Configuración MQTT  

BROKER = "tu-servidor-mqtt.com"
TOPIC = "tanques/datos"

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    print("Mensaje recibido:", data)

    try:
        tanque = Tanque.objects.get(id=data["tanque_id"])
        
        for tipo_sensor, valor in data["sensores"].items():
            sensor = Sensor.objects.get(tanque=tanque, tipo=tipo_sensor)
            Medicion.objects.create(sensor=sensor, valor=valor)

    except Exception as e:
        print("Error al procesar datos MQTT:", str(e))

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)

client.loop_forever()
