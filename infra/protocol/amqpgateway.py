from application.model.request.amqprequest import AMQPRequest
from config.log import logger
from domain.aggregate.metadata.valueobject import networkprotocol, transportprotocol
from infra.util.packetlistener import start_packet_listener


def run_amqp_gateway(receive_buffer=4096):
    def target_function(client_socket, client_address):
        logger.info(f"AMQP connection received from {client_address}")
        try:
            while True:
                data = client_socket.recv(receive_buffer)
                if not data:
                    logger.warning("AMQP client disconnected")
                    break

                # Decode AMQP data
                amqp_request = AMQPRequest()
                amqp_request.decode(data)
                logger.info(f"Received AMQP data from {client_address}: {amqp_request}")

        except Exception as e:
            logger.warning(f"Error handling AMQP client {client_address}: {e}")
        finally:
            client_socket.close()
            logger.info(f"AMQP connection closed with {client_address}")

    start_packet_listener(port=5672,
                          target_function=target_function,
                          network_protocol=networkprotocol.IPv4,
                          transport_protocol=transportprotocol.TCP)
