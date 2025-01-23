from application.model.request.mqttrequest import MQTTRequest
from config.log import logger
from domain.aggregate.metadata.valueobject import networkprotocol, transportprotocol
from infra.util.packetlistener import start_packet_listener


def run_mqtt_gateway(receive_buffer=4096):
    def target_function(client_socket, client_address):
        logger.info(f"MQTT connection received from {client_address}")
        try:
            while True:
                data = client_socket.recv(receive_buffer)
                if not data:
                    logger.warning("MQTT client disconnected")
                    break

                # Decode MQTT data
                mqtt_request = MQTTRequest()
                mqtt_request.decode(data)
                logger.info(f"Received MQTT data from {client_address}: {mqtt_request}")

        except Exception as e:
            logger.warning(f"Error handling MQTT client {client_address}: {e}")
        finally:
            client_socket.close()
            logger.info(f"MQTT connection closed with {client_address}")

    start_packet_listener(port=1883,
                          target_function=target_function,
                          network_protocol=networkprotocol.IPv4,
                          transport_protocol=transportprotocol.TCP)
