# movie_service/utils.py
from config import rabbit_user, rabbit_host, rabbit_pass
import pika
import uuid
import json  # Import json for serialization

def get_rabbitmq_channel():
    # Assuming rabbit_user, rabbit_pass, and rabbit_host are defined
    credentials = pika.PlainCredentials(rabbit_user, rabbit_pass)
    parameters = pika.ConnectionParameters(host=rabbit_host, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    return connection, connection.channel()

class RpcClient(object):
    def __init__(self):
        self.connection, self.channel = get_rabbitmq_channel()
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = json.loads(body)  # Deserialize JSON response

    def call(self, category_id):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='category_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(category_id)
        )
        while self.response is None:
                self.connection.process_data_events()
        return self.response

    def close(self):
        self.connection.close()
