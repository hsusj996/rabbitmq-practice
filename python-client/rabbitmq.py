import pika

connection_params = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=pika.PlainCredentials('guest', 'guest')
)

connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.queue_declare(queue='queue')

def callback(ch, method, properties, body):
    print(f'Received: {body.decode()}')
    
channel.basic_consume(
    queue='queue',
    on_message_callback=callback,
    auto_ack=True
)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()