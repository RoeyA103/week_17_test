from kafka_consumer import *
from sql_service import get_conn_cursor , int_db


topic = os.getenv("TOPIC","OrCu")

conn , cursor = get_conn_cursor()

def main():
    int_db(conn=conn,cursor=cursor)
    consumer = get_consumer(topic=topic)
    consumer_listener(consumer=consumer)


if __name__=="__main__":
    main()