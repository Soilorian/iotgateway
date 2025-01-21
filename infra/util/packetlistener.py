import socket
import threading

from domain.aggregate.metadata.valueobject import networkprotocol, transportprotocol
from config.log import logger


def start_packet_listener(
        port: int,
        target_function,
        network_protocol: networkprotocol,
        transport_protocol: transportprotocol,
        socket_layer=socket.SOL_SOCKET,
        socket_reuse=socket.SO_REUSEADDR,
        reuse_value=1,
        host_addr="127.0.0.1",
        receive_buffer=4096,
        backlog=5,
):
    server_socket = socket.socket(network_protocol, transport_protocol)
    server_socket.setsockopt(socket_layer, socket_reuse, reuse_value)
    server_socket.bind((host_addr, port))
    if transport_protocol == transportprotocol.TCP:
        server_socket.listen(backlog)
    logger.info(f"Listening for incoming connections on port {port}...")

    try:
        while True:
            if transport_protocol == transportprotocol.UDP:
                target_function(server_socket, None)
                data, address = server_socket.recvfrom(receive_buffer)
                if data:
                    target_function(data, address, server_socket)
            elif transport_protocol == transportprotocol.TCP:
                client_socket, client_address = server_socket.accept()
                client_thread = threading.Thread(target=target_function, args=(client_socket, client_address), daemon=True)
                client_thread.start()
    except KeyboardInterrupt:
        logger.info(f"\nShutting down the packet listener for port {port}.")
    finally:
        server_socket.close()