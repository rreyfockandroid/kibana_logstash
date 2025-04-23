from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError
import msgpack
import json
import logging
from kafka.cluster import ClusterMetadata

logger = logging.getLogger('kafka_producer')

BROKER = 'kafka:9092'
TOPIC = 'test-topic'

def consumer():
    consumer = KafkaConsumer(
        TOPIC,
        group_id='my-group',
        bootstrap_servers=[BROKER]
    )
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))


if __name__ == "__main__":
    consumer()