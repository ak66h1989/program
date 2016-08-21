# should initialize mongodb first

from pymongo import *
from pymongo import MongoClient
client = MongoClient()
db = client.test
collection = db.['test1']
collection.find_one()
collection.find()
for post in collection.find():
    print(post)

import datetime

post = {"author": "mi",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

# create collection '中文' and insert data
posts = db.['中文']
posts.insert_one(post)

db.collection_names(include_system_collections=False) # list collection

