from pymongo import  errors
from mongo_connection import get_collectin 


def load_data():
    collection = get_collectin()


def mongo_stream(collection, batch_size=3,jump=1):
    try:
        docs = list(collection.aggregate([{"$unset": "_id"},
                                          {"$skip":jump},
                                          {"$limit":batch_size}]))

        print(docs)
        print("read data from mongo successfuly")

        return docs
    except errors.PyMongoError as e:
        raise e

       
        
