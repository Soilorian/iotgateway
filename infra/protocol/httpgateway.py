from config.log import logger
from infra.util.packetlistener import start_packet_listener
from domain.aggregate.metadata.valueobject import networkprotocol, transportprotocol
from application.gatewaycontroller import consume_http_request
from application.model.request.httprequest import HttpRequest

def run_http_gateway(receive_buffer=4096):
    def target_function(client_socket, client_address):
        logger.info(f"http connection received from {client_address}")
        try:
            while True:
                data = client_socket.recv(receive_buffer)
                if not data:
                    logger.warning("http client disconnected")
                    break

                logger.info(f"Received http data from {client_address}:")
                data = data.decode('utf-8', errors='ignore')
                request = HttpRequest()
                request.decode(data)
                print(data)
                consume_http_request(request)

        except Exception as e:
            logger.warning(f"Error handling http client {client_address}: {e}")
        finally:
            client_socket.close()
            logger.info(f"Connection closed with {client_address}")

    start_packet_listener(port=8080,
                          target_function=target_function,
                          network_protocol=networkprotocol.IPv4,
                          transport_protocol=transportprotocol.TCP)
