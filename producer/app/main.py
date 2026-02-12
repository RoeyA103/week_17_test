import kafka_publisher
from mongo_connection import get_collectin
import mongo_service
import os
from time import sleep

topic = os.getenv("TOPIC","OrCu")

def main():
    sleep(20)
    jump = 0
    batch_size=30
    collection = get_collectin()
    producer = kafka_publisher.get_producer()

    while True:
        docs = mongo_service.mongo_stream(collection=collection
                                          ,batch_size=batch_size
                                          ,jump=jump)

        if not docs:
            print("No more documents — exit")
            break
        
        for doc in docs:
            kafka_publisher.send_message(producer=producer,topic=topic,message=doc)
            sleep(0.5)

        jump += batch_size    

        
if __name__ == "__main__":
    main()