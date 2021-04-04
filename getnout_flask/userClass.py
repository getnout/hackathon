from flask_mongoengine import MongoEngine
from pymongo.mongo_client import MongoClient


class User():
    def __init__(self, collection, userName):
        self.userName = userName
        self.collection = collection
        self.contact1 = []
        self.contact2 = []
        self.contact3 = []
        pass
    
    def ParseContacts(self):
        
        doc = self.collection.find_one({"userName": self.userName})
        
        self.contact1 = [doc['contact1']['name'],  doc['contact1']['phoneNumber'], doc['contact1']['relationship']]
        self.contact2 = [doc['contact2']['name'],  doc['contact2']['phoneNumber'], doc['contact2']['relationship']]
        self.contact3 = [doc['contact3']['name'],  doc['contact3']['phoneNumber'], doc['contact3']['relationship']]

    

