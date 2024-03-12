import pika
import json
import threading
from config import rabbit_user, rabbit_host, rabbit_pass
def callback(ch, method, properties, body):
    category_id = json.loads(body)

    category_info = {'id': category_id, 'name': 'Example Category'}    
   
    ch.basic_publish(exchange='',   
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id = properties.correlation_id),
                     body=json.dumps(category_info))
    

    # ch.basic_ack(delivery_tag=method.delivery_tag)
   
    print("category_info", category_info)        

    return category_info           


def start_consumer_thread():
    def run():
        credentials = pika.PlainCredentials(rabbit_user, rabbit_pass)
        parameters = pika.ConnectionParameters(host=rabbit_host, credentials=credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        channel.queue_declare(queue='category_queue')

        channel.basic_consume(queue='category_queue',
                              auto_ack=False,
                              on_message_callback=callback)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
        connection.close()

    consumer_thread = threading.Thread(target=run)
    consumer_thread.start()

# def start_consumer():
#     credentials = pika.PlainCredentials(rabbit_user, rabbit_pass)
#     parameters = pika.ConnectionParameters(host=rabbit_host, credentials=credentials)
#     connection = pika.BlockingConnection(parameters)
#     channel = connection.channel()

#     channel.queue_declare(queue='category_queue')

#     channel.basic_consume(queue='category_queue',
#                           auto_ack=False,
#                           on_message_callback=callback)

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()