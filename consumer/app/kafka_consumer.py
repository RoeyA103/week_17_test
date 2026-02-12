import json
from confluent_kafka import Consumer 
import os
from sql_service import inser_data
from time import sleep

bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS","localhost:9092")

def get_consumer(topic:str,auto_offset_reset="earliest"):
    consumer_config = {
        "bootstrap.servers": bootstrap_servers,
        "group.id": f"{topic}-tracker",
        "auto.offset.reset": auto_offset_reset
    }

    consumer = Consumer(consumer_config)

    consumer.subscribe([topic])

    print(f"🟢 Consumer is running and subscribed to {topic} topic")  
    
    return consumer


def consumer_listener(consumer):
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("❌ Error:", msg.error())
                continue

            value = msg.value().decode("utf-8")

            data = json.loads(value)

            inser_data(data=data)

            sleep(1)
            
    except KeyboardInterrupt:
        print("\n🔴 Stopping consumer")

    finally:
        consumer.close()

