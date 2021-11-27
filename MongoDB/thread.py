import pymongo 
import threading
from dotenv import load_dotenv
from os import getenv
load_dotenv()
cluster = pymongo.MongoClient(getenv("client_details"))
db = cluster.test
collection = db.test
a = {'alias': "Abhishek", 'message': "I am awesome"}
collection.insert_one(a)

