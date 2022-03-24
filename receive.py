import pika, sys, os


def main():
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Create a queue
    channel.queue_declare(queue='hello')

    # Receive messages
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)

    # Start consuming
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


# Execute main()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nBye!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
