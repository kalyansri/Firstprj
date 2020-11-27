#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
# The default exchange is implicitly bound to every queue, with a routing key equal to the queue name.
# It is not possible to explicitly bind to, or unbind from the default exchange. It also cannot be deleted.
channel.basic_publish(exchange='', routing_key='hello', body='Hello World8!')
print(" [x] Sent 'Hello World 55558885!'")
connection.close()