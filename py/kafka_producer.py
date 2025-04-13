from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError
import msgpack
import json
import logging
from kafka.cluster import ClusterMetadata
import config as conf

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
    producer = KafkaProducer(bootstrap_servers=[BROKER])
    producer.send(TOPIC, b'costam').add_callback(on_send_success).add_errback(on_send_error)

if __name__ == "__main__":
    conf.config()
    producer()  