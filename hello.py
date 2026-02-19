import pika
import os
import time

# Get the broker address from the environment variable we set in Compose
broker_host = os.getenv("BROKER_URL", "localhost")

# Get user/pass from environment, or use defaults
user = os.getenv("RABBIT_USER", "guest")
password = os.getenv("RABBIT_PASS", "guest")

print(f"Connecting to RabbitMQ at {broker_host} as user {user}...")

credentials = pika.PlainCredentials(user, password)
parameters = pika.ConnectionParameters(host=broker_host, credentials=credentials)

# Middleware logic: Retry until the broker is ready
while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=broker_host))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        print(" Successfully connected to the Broker!")
        break
    except Exception as e:
        print("Broker not ready yet... retrying in 5 seconds")
        time.sleep(5)

print("Sending a test message: 'Hello World!'")
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
connection.close()
time.sleep(100)
