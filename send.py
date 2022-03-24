from datetime import datetime

import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue
channel.queue_declare(queue='hello')

# Define current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# Define message
message = 'Hello World! Current time is: ' + current_time

# Send a message to the queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(f" [x] Sent {message}")

# Close the connection
connection.close()
