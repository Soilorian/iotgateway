from config.log import logger
from infra.util.packetlistener import start_packet_listener
from domain.aggregate.metadata.valueobject import networkprotocol, transportprotocol


def run_coap_gateway(receive_buffer=4096):
    def target_function(server_socket, client_address):
        logger.info(f"CoAP message received from {client_address}")
        try:
            while True:
                data, address = server_socket.recvfrom(receive_buffer)
                if not data:
                    logger.warning("No CoAP data received, client might have disconnected.")
                    break

                logger.info(f"Received CoAP data from {address}:")
                print(data)

                ack_message = b"\x60\x00\x00\x00"
                server_socket.sendto(ack_message, address)
                logger.info(f"Sent acknowledgment to {address}")

        except Exception as e:
            logger.warning(f"Error handling CoAP message from {client_address}: {e}")

    start_packet_listener(port=5683,
                          target_function=target_function,
                          network_protocol=networkprotocol.IPv4,
                          transport_protocol=transportprotocol.UDP)
