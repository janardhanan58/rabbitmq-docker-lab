import pika
import os

broker_host = os.getenv("BROKER_URL", "rabbitmq")
connection = pika.BlockingConnection(pika.ConnectionParameters(host=broker_host))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f" [x] Received: {body.decode()}")

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
