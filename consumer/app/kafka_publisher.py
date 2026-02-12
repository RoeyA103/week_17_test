import json
import os
from confluent_kafka import Producer ,error

bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS","localhost:9092")



def get_producer():
    try:
        producer_config = {
            "bootstrap.servers": bootstrap_servers
        }

        producer = Producer(producer_config)
        print("connection to kafka succsses")
        return producer
    
    except error.ProduceError as e:
        raise e

def send_message(producer,topic: str, message: dict):

    def delivery_report(err, msg):
        if err:
            print(f"❌ Delivery failed: {err}")
        else:
            print(
                f"✅ Delivered {msg.value().decode('utf-8')} \n"
                f"to {msg.topic()} : partition {msg.partition()} : offset {msg.offset()}"
            )

    value = json.dumps(message).encode("utf-8")

    producer.produce(topic=topic, value=value, callback=delivery_report)

    producer.flush()

    producer.poll(0)

    print("successfuly send")




