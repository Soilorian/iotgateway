import unittest
import requests
import asyncio
from aiocoap import Message, Context
import paho.mqtt.client as mqtt
import pika


# Sender functions
def send_http_message(url, message):
    response = requests.post(url, json={"message": message})
    return response.status_code, response.content


def send_coap_message(uri, message):
    async def coap_client():
        protocol = await Context.create_client_context()
        request = Message(code=1, uri=uri, payload=message.encode('utf-8'))
        response = await protocol.request(request).response
        return response.code, response.payload.decode('utf-8')

    return asyncio.run(coap_client())


def send_mqtt_message(broker, port, topic, message):
    client = mqtt.Client()
    client.connect(broker, port, 60)
    client.publish(topic, message)
    client.disconnect()
    return True


def send_amqp_message(broker, port, queue, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=broker, port=port))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='', routing_key=queue, body=message)
    connection.close()
    return True


class TestSenders(unittest.TestCase):
    def test_http_sender(self):
        status_code, response = send_http_message("http://localhost:8080/http-receiver", "Test HTTP Message")
        self.assertEqual(status_code, 200)
        self.assertIn(b'message', response)

    def test_coap_sender(self):
        code, payload = send_coap_message("coap://localhost/resource", "Test CoAP Message")
        self.assertEqual(code, 69)  # 2.05 Changed
        self.assertEqual(payload, b'test')

    def test_mqtt_sender(self):
        result = send_mqtt_message("mqtt.example.com", 1883, "test/topic", "Test MQTT Message")
        self.assertTrue(result)

    def test_amqp_sender(self):
        result = send_amqp_message("amqp.example.com", 5672, "test_queue", "Test AMQP Message")
        self.assertTrue(result)


if __name__ == '__main__':
    #unittest.main()
    send_mqtt_message("localhost", 1883, "test/topic", "Test MQTT Message")
