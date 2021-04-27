# amqps://qykxrwyg:Ka8uohnlDq6luS0H3U7knhdm3pqYO2kc@clam.rmq.cloudamqp.com/qykxrwyg
import pika # package to enable sending events

params = pika.URLParameters('amqps://qykxrwyg:Ka8uohnlDq6luS0H3U7knhdm3pqYO2kc@clam.rmq.cloudamqp.com/qykxrwyg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')

# routing_key: the queue we want to send the event