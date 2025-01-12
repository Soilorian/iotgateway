import logging
import threading

import paho.mqtt.client as mqtt

# MQTT Configuration
MQTT_BROKER = "mqtt.example.com"
MQTT_PORT = 1883
MQTT_TOPIC = "example/topic"


# MQTT on_message callback
def on_mqtt_message(client, userdata, msg):
    print(f"MQTT: Received message on topic {msg.topic}: {msg.payload.decode('utf-8')}")


# Initialize MQTT client
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_mqtt_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.subscribe(MQTT_TOPIC)

# Start MQTT loop in a separate thread
mqtt_thread = threading.Thread(target=lambda: mqtt_client.loop_forever(), daemon=True)
mqtt_thread.start()
print("started mqtt receiver")
