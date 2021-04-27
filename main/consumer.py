import pika # package to enable sending events

params = pika.URLParameters('amqps://qykxrwyg:Ka8uohnlDq6luS0H3U7knhdm3pqYO2kc@clam.rmq.cloudamqp.com/qykxrwyg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Receive in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming')
channel.start_consuming()

channel.close()