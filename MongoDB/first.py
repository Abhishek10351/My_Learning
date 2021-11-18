import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
cluster = pymongo.MongoClient(os.environ['CHANGE_STREAM_DB'])
db = cluster.test
collection = db["test"]


post = {"name":"Daima"}
#post2 = {"name":"Uthri", "dob": "20-01-2003"}
#collection.insert_one(post)
