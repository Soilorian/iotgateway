import threading

from infra.httpgateway import run_http_gateway
from infra.coapgateway import run_coap_gateway


def start_gateway():
    http_thread = threading.Thread(target=run_http_gateway)
    coap_thread = threading.Thread(target=run_coap_gateway())
    http_thread.start()
    coap_thread.start()
