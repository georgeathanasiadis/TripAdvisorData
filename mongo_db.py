import os
import json
from dotenv import load_dotenv
from pymongo import MongoClient


'''
    This function connects to the local MongoDB server, create a local database and a local collection.
    It returns the collection.
'''
def create_mongo():
    # connect to local MongoDB server
    load_dotenv("config.env")
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    client = MongoClient("mongodb://" + MONGO_USER + ":" + MONGO_PASSWORD + "@localhost:27017")

    # create a local database
    db = client['TripAdvisor']

    # create a collection
    collection = db['Restaurant_reviews']

    return collection


'''
    This function inserts a given dictionary to a given mongo collection.
'''
def insert_to_mongo(collection, dictionary):
    collection.insert_one(dictionary)
