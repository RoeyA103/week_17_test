from kafka_consumer import *


def main():
    consumer = get_consumer()
    consumer_listener(consumer=consumer)
    