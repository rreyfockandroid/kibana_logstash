LOGSTASH_BIN=/usr/local/sbin/logstash-8.17.4/bin
LOGSTASH_CONF=/home/grzegorz/Projects/kibana_logstash/kafka-to-es.conf
LOGSTASH_MANY_CONF=/home/grzegorz/Projects/kibana_logstash/kafka-to-es_many.conf

KAFKA_TOPIC_NAME=test-topic
CMD=docker exec --workdir /bin -it kafka 
SERVER=--bootstrap-server localhost:9092

kafka-group-list:
	${CMD} kafka-consumer-groups ${SERVER} --list

kafka-group-describe:
	${CMD} kafka-consumer-groups ${SERVER} --describe --group logstash-group

kafka-topic-list:
	${CMD} kafka-topics ${SERVER} --list

kafka-consumer:
	${CMD} kafka-console-consumer ${SERVER} --topic ${KAFKA_TOPIC_NAME}

kafka-producer:
	${CMD} kafka-console-producer ${SERVER} --topic ${KAFKA_TOPIC_NAME}

logstash-run:
	cd ${LOGSTASH_BIN}; ./logstash -f ${LOGSTASH_CONF}

logstash-many-run:
	cd ${LOGSTASH_BIN}; ./logstash -f ${LOGSTASH_MANY_CONF}

all-run:
	docker-compose start

elasticsearch-indexes:
	curl -X GET "http://localhost:9200/_cat/indices?v"