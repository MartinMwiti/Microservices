import pika # package to enable sending events
import json

from main import Product, db

params = pika.URLParameters('amqps://qykxrwyg:Ka8uohnlDq6luS0H3U7knhdm3pqYO2kc@clam.rmq.cloudamqp.com/qykxrwyg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Receive in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        # create product
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('Product Created')
    
    elif properties.content_type == 'product_updated':
        # updating product
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('Product Updated')

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data) # in this case data == id
        db.session.delete(product)
        db.session.commit()
        print('Product Deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True) # auto_act=True makes sure we consume the messages

print('Started Consuming')
channel.start_consuming()

channel.close()