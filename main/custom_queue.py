import models
# import pika

QUEUE_NAME = 'links'


def send_message_to_queue_1(link: models.Link):
    return None
    # connection = pika.BlockingConnection(
    #     pika.ConnectionParameters(host='localhost'))
    # channel = connection.channel()
    #
    # channel.queue_declare(queue=QUEUE_NAME)
    #
    # channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    # print(" [x] Sent 'Hello World!'")
    # connection.close()