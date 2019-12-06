from pymongo import MongoClient
import xmltodict
import xml.etree.ElementTree as ET


# MAIN
def connection_system_path(): # Plugin and main dependencies
    client=MongoClient('localhost',27017)
    db=client.beat
    post=db.System
    return post

def uploadSystem(xml): # also on beatmain.py
    my_dict = xmltodict.parse(xml)
    posts = connection_system_path()
    result = posts.insert_one(my_dict)

def is_system_empty():
    projects = connection_system_path()
    projectsList = projects.find()
    list_of_projects = []
    for item in projectsList:
        list_of_projects.append(item['System'])
    if list_of_projects==[]:
        return True
    else:
        return False
