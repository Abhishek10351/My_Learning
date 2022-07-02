import pymongo
from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()
cluster = pymongo.MongoClient(getenv("client_details"))
collection = cluster.test.test
print("watching")

#a = collection.watch([{'$match': {'operationType': 'insert'}}])
def new_msg_check(self):
    '''checks for new messages, and displays alert on the screen'''
    db.watch([{'$match': {'operationType': 'insert'}}])
    def get_messages() -> list:
        """gets all the messages from the server """
        for messages in db.find({}):
            yield f"[{messages['alias']}]: {messages['message']}"
    self.msg_box.setText("\n".join(get_messages()))
for change in change_stream:
    print(change)
    print('')
post = {"name":"Daima"}
#post2 = {"name":"Uthri", "dob": "20-01-2003"}
#collection.insert_one(post)
