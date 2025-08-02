from application.gatewaycontroller import consume_coap_request
from application.model.request.coaprequest import CoapRequest
from config.log import logger
from domain.aggregate.metadata.valueobject import networkprotocol, transportprotocol
from infra.protocol.model.response.CoapResponse import encode_coap_response
from infra.util.packetlistener import start_packet_listener


def run_coap_gateway(receive_buffer=4096):
    def target_function(data, address, server_socket):
        logger.info(f"CoAP message received from {address}")

        try:
            logger.info(f"Received CoAP data from {address}: {data}")
            try:
                # Decode the request
                coap_request = CoapRequest()
                coap_request.decode(data, address)
                logger.info(f"Decoded CoAP request: {coap_request}")
                # Call consume_coap_request and get response
                coap_response_dto = consume_coap_request(coap_request)
                # Encode response into raw bytes
                response_bytes = encode_coap_response(coap_response_dto, coap_request.token)
                # Send response
                server_socket.sendto(response_bytes, address)
                logger.info(f"Sent CoAP response to {address}: {coap_response_dto}")
            except Exception as e:
                logger.error(f"Error processing CoAP request from {address}: {e}")
        except Exception as e:
            logger.warning(f"Error handling CoAP message from {address}: {e}")

    start_packet_listener(port=5683,
                          target_function=target_function,
                          network_protocol=networkprotocol.IPv4,
                          transport_protocol=transportprotocol.UDP)
