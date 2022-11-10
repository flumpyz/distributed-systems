import json
import os

import models
import pika

QUEUE_NAME = 'links'


def send_message_to_queue(link: models.Link):
    connection = pika.BlockingConnection(pika.URLParameters(os.environ['RABBITMQ_URL']))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)

    web_request_body = {
        'id': str(link.id),
        'url': link.url
    }
    body_str = json.dumps(web_request_body)
    body_bytes = bytes(body_str, 'utf-8')

    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=body_bytes)
    connection.close()
