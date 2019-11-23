from pymongo import MongoClient
import xmltodict
import pprint
import json
import xml.etree.ElementTree as ET


def uploadXML(xml):
    client = MongoClient('localhost', 27017)
    db = client.pymongo_test
    my_dict = xmltodict.parse(xml)
    posts = db.posts
    result = posts.insert_one(my_dict)

def uploadDataSet(xml):
    client = MongoClient('localhost', 27017)
    db = client.pymongo_test
    my_dict = xmltodict.parse(xml)
    dataSet = db.dataSet
    result = dataSet.insert_one(my_dict)

def retrieve_list_of_projects():
    client = MongoClient('localhost', 27017)
    db = client.pymongo_test
    projects = db.posts
    projectsList = projects.find()
    list_of_projects = []
    for item in projectsList:
        list_of_projects.append(item['Project']['Project_name']['#text'])
    return list_of_projects


def retrieve_selected_project(project_name):
    client = MongoClient('localhost', 27017)
    db = client.pymongo_test
    projects = db.posts
    projectsList = projects.find()

    for item in projectsList:
        if item['Project']['Project_name']['#text'] == project_name:
            return item


def delete_selected_project(nameofProject):
    client = MongoClient('localhost', 27017)
    db = client.pymongo_test
    projects = db.posts
    myquery = {"Project.Project_name.#text": nameofProject}
    projects.delete_one(myquery)
    
# holder element of where to place xml2
def xmlmerger(holder, xml1, xml2):
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    for element1 in xml1.findall(holder):
        element1.append(xml2)
    ET.dump(xml1)
    print(xml1)
    print("+++++++++++++++++++++++++++++++++++++++++++++++")