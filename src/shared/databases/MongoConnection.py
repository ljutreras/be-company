from pymongo import MongoClient
import src.app.config.index as config


class MongoConnection:
    def create():
        client = MongoClient(config.MONGO_URL)
        db = client[config.DB_NAME]
        collection = db[config.DB_COLLECTION]
        return collection