from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError
import time
import json
import logging
from kafka.cluster import ClusterMetadata
import conf.config as conf

logger = logging.getLogger('kafka_producer')

BROKER = 'kafka:9092'
TOPIC = 'test-topic'

def on_send_success(record_metadata):
    logger.info(f''' 
        {record_metadata}
        topic: {record_metadata.topic} 
        partition: {record_metadata.partition} 
        offset: {record_metadata.offset}'''
    )

def on_send_error(excp):
    logger.error(f'message send error: {excp}')

def producer():
    return KafkaProducer(bootstrap_servers=[BROKER])
    

def send(producer, topic):
    producer.send(topic, b'costam').add_callback(on_send_success).add_errback(on_send_error)

def produce_from_file(producer, file, topic):
    with open(file, 'r') as file:
        for line in file:
            fn = lambda x: json.dumps(json.loads(x)).encode('utf-8')
            producer.send(topic, value=fn(line)).add_callback(on_send_success).add_errback(on_send_error)
            time.sleep(1)

if __name__ == "__main__":
    conf.config()
    producer = producer()
    # produce_from_file(producer, '../data/books_openlib.json')
    produce_from_file(producer, '../data/googleapis_books.json', TOPIC)
    producer.flush()
    producer.close()  