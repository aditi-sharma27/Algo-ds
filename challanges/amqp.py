import pika
import json
import os


AMQPUSERNAME = "guest"
AMQPPASSWORD = "guest"
AMQPHOST = "127.0.0.1"
AMQPPORT = 15672


class RabbitAMQP(object):
    def __init__(self, user, password, host, port):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def get_connection(self):
        credentials = pika.PlainCredentials(self.user, self.password)
        params = pika.ConnectionParameters(host=self.host)
        self.conn = pika.BlockingConnection(params)
        channel = self.conn.channel()
        return channel

    def declare_exchange(self, exchange_name, exc_type):
        channel = self.get_connection()
        channel.exchange_declare(exchange=exchange_name, exchange_type=exc_type)
        self.conn.close()

    def declare_queue(self, exchange_name, queue_name, routing_key):
        channel = self.get_connection()
        channel.queue_declare(queue=queue_name)
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

        self.conn.close()

    def send_message(self, exchange_name, routing_key, msg):
        # ch.exchange_declare(exchange='smbtest1',
        #                      exchange_type='fanout')
        # result = ch.queue_declare(queue='mqtest1')
        channel = self.get_connection()
        channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=msg)
        print(" [x] Sent", msg)
        self.conn.close()

    @staticmethod
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    def consume_msg(self, exc_name, routing, queue_name):
        channel = self.get_connection()
        #channel.queue_bind(exchange='smbtest', queue=queue_name, routing_key='test')

        print(' [*] Waiting for messages. To exit press CTRL+C')

        channel.basic_consume(queue=queue_name, on_message_callback=self.callback, auto_ack=True)

        channel.start_consuming()


if __name__ == '__main__':
    exc_name = "smbtest"
    routing="test"
    a= RabbitAMQP(AMQPUSERNAME, AMQPPASSWORD, AMQPHOST, AMQPPORT)
    # a.declare_queue(exc_name, 'mqtest', routing)
    # a.declare_queue(exc_name, 'mqtest1', routing)
    a.send_message(exc_name, routing, "hi12")
    #a.consume_msg(exc_name, routing, "mqtest")
    a.send_message(exc_name, routing, "hi13")
    #a.consume_msg(exc_name, routing, "mqtest1")

## map project is --- to fun--- read the cof file ---match/or not match---if not 
##
