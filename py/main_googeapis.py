import conf.config as cfg
import kafka_clt.kafka_producer as ka

TOPIC = 'google-topic'

if __name__ == "__main__":
    cfg.config()
    producer = ka.producer()
    ka.produce_from_file(producer, '../data/googleapis_books.json', TOPIC)
    producer.flush()
    producer.close()  