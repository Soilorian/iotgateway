from config.log import logger
from domain.aggregate.metadata.model.dto.httpresponsedto import HttpResponseDto
from infra.protocol.model.response.HttpResponse import encode_http_response
from infra.util.packetlistener import start_packet_listener
from domain.aggregate.metadata.valueobject import networkprotocol, transportprotocol
from application.gatewaycontroller import consume_http_request
from application.model.request.httprequest import HttpRequest


def run_http_gateway(receive_buffer=4096):
    def target_function(client_socket, client_address):
        logger.info(f"HTTP connection received from {client_address}")
        try:
            while True:
                data = client_socket.recv(receive_buffer)
                if not data:
                    logger.warning("HTTP client disconnected")
                    break

                logger.info(f"Received HTTP data from {client_address}:")
                data = data.decode('utf-8', errors='ignore')

                # Decode the HTTP request
                request = HttpRequest()
                request.decode(data, client_address)

                # Process the request and get the response
                response = consume_http_request(request)

                response_data = encode_http_response(response)
                # Send the response back to the client
                client_socket.sendall(response_data)
                logger.info(f"Response sent to {client_address}")
                client_socket.close()

        except Exception as e:
            logger.warning(f"Error handling HTTP client {client_address}: {e}")
        finally:
            client_socket.close()
            logger.info(f"Connection closed with {client_address}")

    start_packet_listener(
        port=8080,
        target_function=target_function,
        network_protocol=networkprotocol.IPv4,
        transport_protocol=transportprotocol.TCP
    )
