package main

import (
	"fmt"
	"log"

	"github.com/IBM/sarama"
)

const (
	broker = "kafka:9092"
	topic  = "test-topic"
)

func main() {
	fmt.Println("start")
	config := sarama.NewConfig()
	config.Producer.Return.Successes = true
	config.Producer.RequiredAcks = sarama.WaitForLocal
	config.Producer.Return.Errors = true

	brokers := []string{broker}
	producer, err := sarama.NewSyncProducer(brokers, config)
	if err != nil {
		log.Fatalf("Failed to create producer: %v", err)
	}
	defer producer.Close()

	msg := &sarama.ProducerMessage{
		Topic: topic,
		Value: sarama.StringEncoder("hello world"),
	}

	partition, offset, err := producer.SendMessage(msg)
	if err != nil {
		log.Printf("Failed to send message: %v", err)
	} else {
		fmt.Printf("Message sent to partition %d at offset %d\n", partition, offset)
	}
}

func async() {
	config := sarama.NewConfig()
	config.Producer.RequiredAcks = sarama.WaitForLocal
	config.Producer.Return.Errors = true

	brokers := []string{"localhost:9092"}
	producer, err := sarama.NewAsyncProducer(brokers, config)
	if err != nil {
		log.Fatalf("Failed to create producer: %v", err)
	}
	defer producer.Close()

	msg := &sarama.ProducerMessage{
		Topic: "test",
		Value: sarama.StringEncoder("Hello, World!"),
	}

	producer.Input() <- msg

	select {
	case success := <-producer.Successes():
		fmt.Printf("Message sent to partition %d at offset %d\n", success.Partition, success.Offset)
	case err := <-producer.Errors():
		log.Printf("Failed to send message: %v", err)
	}
}
