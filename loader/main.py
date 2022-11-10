import json
import os
import sys

import pika
import requests

QUEUE_NAME = 'links'


def handle_message(ch, method, properties, body):
    link_json = json.loads(body.decode('utf-8'))
    response = requests.get(link_json['url'], timeout=10)
    status = response.status_code

    web_url = f'{os.environ["WEB_BASE_URL"]}/links/{link_json["id"]}'
    web_request_body = {
        'status': str(status)
    }
    web_response = requests.put(web_url, json=web_request_body, timeout=10)
    web_response.raise_for_status()


def main():
    connection = pika.BlockingConnection(pika.URLParameters(os.environ['RABBITMQ_URL']))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(queue=QUEUE_NAME, auto_ack=True, on_message_callback=handle_message)
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
