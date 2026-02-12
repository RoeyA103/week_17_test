from pymongo import MongoClient , errors 
import os

mongo_host = os.getenv("MONGO_HOST","mongodb://localhost")
mongo_port = os.getenv("MONGO_PORT",27017)

def get_collectin():
    try:
        client = MongoClient(host=mongo_host,port=int(mongo_port))

        db = client.test17

        collection = db.customers_orders


        print("connect to mongo successfuly")

        return collection
    except errors.PyMongoError as e:
        raise e