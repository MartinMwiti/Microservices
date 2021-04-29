# amqps://qykxrwyg:Ka8uohnlDq6luS0H3U7knhdm3pqYO2kc@clam.rmq.cloudamqp.com/qykxrwyg
import pika # package to enable sending events
import json

params = pika.URLParameters(amqps_KEY)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties) # before sending anything we need to convert it to json before sending

# routing_key: the queue we want to send the event