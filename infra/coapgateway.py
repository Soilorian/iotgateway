import threading
from aiocoap import Context, Message
import asyncio


# Class representing the CoAP server
class CoAPServer:
    def __init__(self, bind_address="0.0.0.0", port=5683):
        self.bind_address = bind_address
        self.port = port
        self.protocol = None

    async def start(self):
        # Create the CoAP server context
        self.protocol = await Context.create_server_context(self, bind=(self.bind_address, self.port))
        print(f"CoAP: Listening for messages on {self.bind_address}:{self.port}")

    async def render_post(self, request):
        # Handle POST requests
        payload = request.payload.decode("utf-8")
        print(f"CoAP: Received message: {payload}")
        return Message(code=2.04, payload=b"Message received")


# Function to start the CoAP server
async def coap_receiver():
    server = CoAPServer()
    await server.start()


# Start the CoAP receiver in a separate thread
def start_coap_receiver():
    coap_thread = threading.Thread(target=lambda: asyncio.run(coap_receiver()), daemon=True)
    coap_thread.start()
    print("CoAP receiver started.")


# Start the server
if __name__ == "__main__":
    start_coap_receiver()
    # Keep the main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nCoAP server shutting down.")
