import pika
import threading

# AMQP Configuration
AMQP_BROKER = "amqp.example.com"
AMQP_PORT = 5672
AMQP_QUEUE = "example_queue"

# Initialize AMQP connection
amqp_connection = pika.BlockingConnection(pika.ConnectionParameters(host=AMQP_BROKER, port=AMQP_PORT))
amqp_channel = amqp_connection.channel()
amqp_channel.queue_declare(queue=AMQP_QUEUE)


# Function to consume messages from AMQP
def consume_amqp_messages():
    def callback(ch, method, properties, body):
        print(f"AMQP: Received message from queue {AMQP_QUEUE}: {body.decode('utf-8')}")

    amqp_channel.basic_consume(queue=AMQP_QUEUE, on_message_callback=callback, auto_ack=True)
    print(f"AMQP: Listening for messages on queue {AMQP_QUEUE}")
    amqp_channel.start_consuming()


# Start AMQP consumer in a separate thread
amqp_thread = threading.Thread(target=consume_amqp_messages, daemon=True)
amqp_thread.start()
print("started amqp receiver")
