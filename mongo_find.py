import pprint
from pymongo import MongoClient

client = MongoClient()
db = client.pchome
coll = db.products
data = coll.find()