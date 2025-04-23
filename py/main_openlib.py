import conf.config as conf
import kafka_clt.kafka_producer as ka

TOPIC = 'openlib-topic'

if __name__ == "__main__":
    conf.config()
    producer = ka.producer()
    ka.produce_from_file(producer, '../data/books_openlib.json', TOPIC)
    producer.flush()
    producer.close()  