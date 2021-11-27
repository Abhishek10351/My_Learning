import pymongo
from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()
cluster = pymongo.MongoClient(getenv("client_details"))
collection = cluster.test.test
print("watching")

#a = collection.watch([{'$match': {'operationType': 'insert'}}])
change_stream = cluster.changestream.collection.watch()
for change in change_stream:
    print(change)
    print('')
post = {"name":"Daima"}
#post2 = {"name":"Uthri", "dob": "20-01-2003"}
#collection.insert_one(post)
