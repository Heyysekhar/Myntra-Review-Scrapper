from pymongo import MongoClient

class MongoOperation:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert_one(self, collection_name, data):
        collection = self.db[collection_name]
        return collection.insert_one(data)

    def find_all(self, collection_name):
        collection = self.db[collection_name]
        return list(collection.find())