import threading

from aiocoap import Message, Context
import asyncio


# Function to receive CoAP messages
async def coap_receiver():
    async def render_post(request):
        payload = request.payload.decode('utf-8')
        print(f"CoAP: Received message: {payload}")
        return Message(code=2.04, payload=b"Message received")

    class CoAPServer:
        def __init__(self):
            self.protocol = None

        async def start(self):
            self.protocol = await Context.create_server_context(self)
            print("CoAP: Listening for messages")

    server = CoAPServer()
    await server.start()


# Start CoAP receiver in a separate thread
coap_thread = threading.Thread(target=lambda: asyncio.run(coap_receiver()), daemon=True)
coap_thread.start()
print("started coap receiver")
