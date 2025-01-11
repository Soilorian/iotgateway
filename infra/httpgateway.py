import asyncio
from flask import Flask, request, Response
from aiocoap import Message, Context
from aiocoap.numbers.codes import Code
import threading

app = Flask(__name__)
subscribers = []  # List of active subscribers


# CoAP client setup
async def send_coap_request(coap_method, uri, payload=None):
    protocol = await Context.create_client_context()
    request = Message(code=coap_method, uri=uri)
    if payload:
        request.payload = payload.encode('utf-8')
    response = await protocol.request(request).response
    return response


# Helper function to send updates to subscribers
def notify_subscribers(update):
    for subscriber in subscribers:
        try:
            subscriber.put(update)
        except Exception as e:
            print(f"Failed to notify subscriber: {e}")


# Endpoint for HTTP clients to subscribe (SSE)
@app.route("/subscribe", methods=["GET"])
def subscribe():
    def event_stream():
        queue = asyncio.Queue()
        subscribers.append(queue)
        try:
            while True:
                update = queue.get_nowait()
                yield f"data: {update}\n\n"
        except asyncio.QueueEmpty:
            pass
        finally:
            subscribers.remove(queue)

    return Response(event_stream(), content_type="text/event-stream")


# Endpoint for CoAP resource updates
@app.route("/publish", methods=["POST"])
def publish():
    data = request.json
    update = data.get("update")
    notify_subscribers(update)
    return {"message": "Update sent to subscribers"}, 200


# CoAP subscription simulation (observe resource)
@app.route("/observe/<path:coap_uri>", methods=["GET"])
def observe_coap(coap_uri):
    async def observe_resource(uri):
        protocol = await Context.create_client_context()
        request = Message(code=Code.GET, uri=f"coap://{uri}")
        request.opt.observe = 0  # CoAP Observe option
        requester = protocol.request(request)
        async for response in requester.observation:
            notify_subscribers(response.payload.decode('utf-8'))

    # Start observing in a background thread
    threading.Thread(target=lambda: asyncio.run(observe_resource(coap_uri))).start()
    return {"message": f"Subscribed to CoAP resource: {coap_uri}"}, 200


if __name__ == "__main__":
    app.run(debug=True)
