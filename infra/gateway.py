import threading

from infra.protocol.amqpgateway import run_amqp_gateway
from infra.protocol.httpgateway import run_http_gateway
from infra.protocol.coapgateway import run_coap_gateway
from infra.protocol.mqttgateway import run_mqtt_gateway


def start_gateway():
    http_thread = threading.Thread(target=run_http_gateway)
    coap_thread = threading.Thread(target=run_coap_gateway)
    amqp_thread = threading.Thread(target=run_amqp_gateway)
    mqtt_thread = threading.Thread(target=run_mqtt_gateway)
    http_thread.start()
    coap_thread.start()
    mqtt_thread.start()
    amqp_thread.start()
