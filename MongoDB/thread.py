import pymongo 
import threading
cluster = pymongo.MongoClient(host="mongodb+srv://deep:1234abcd@cluster.ds3cv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['socialmedia']['messages']
db_log = cluster['socialmedia']['log']
a = {'alias': "Abhishek", 'message': "I am awesome"}
db.insert_one(a)
print("damn")
