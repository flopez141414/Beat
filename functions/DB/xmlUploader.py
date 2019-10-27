from pymongo import MongoClient
import xmltodict
import pprint
import json

def uploadXML(xml):
    client = MongoClient('localhost', 27017)
    print(client)
    db = client.pymongo_test
    print(db)

    my_dict= xmltodict.parse(xml)
    posts = db.posts
    result = posts.insert_one(my_dict)
    print('One post: {0}'.format(result.inserted_id))
