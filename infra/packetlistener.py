import socket
import threading

from domain.valueobject import networkprotocol, transportprotocol
from config.log import logger


def start_packet_listener(
        port: int,
        target_function,
        network_protocol: networkprotocol,
        transport_protocol: transportprotocol,
        backlog=5,
        socket_layer=socket.SOL_SOCKET,
        socket_reuse=socket.SO_REUSEADDR,
        reuse_value=1,
        host_addr="127.0.0.1",
):
    server_socket = socket.socket(network_protocol, transport_protocol)
    server_socket.setsockopt(socket_layer, socket_reuse, reuse_value)
    server_socket.bind((host_addr, port))
    logger.info(f"Listening for incoming connections on port {port}...")

    try:
        while True:
            if transport_protocol == transportprotocol.UDP:
                # Directly call the target function for datagrams
                target_function(server_socket, None)
            else:
                # Accept an incoming connection (TCP case)
                client_socket, client_address = server_socket.accept()
                client_thread = threading.Thread(target=target_function, args=(client_socket, client_address), daemon=True)
                client_thread.start()
    except KeyboardInterrupt:
        logger.info(f"\nShutting down the packet listener for port {port}.")
    finally:
        server_socket.close()