from pymongo import MongoClient
import xmltodict
import pprint
import json

#XML libraries
import xml.etree.ElementTree as ET
import xmltodict
import pprint
import json

def connectionProjectPath:
    client = MongoClient('localhost', 27017)
    # print(client)
    db = client.BEAT


def uploadXML(xml):
    client = MongoClient('localhost', 27017)
    # print(client)
    db = client.BEAT
    # print(db)

    my_dict = xmltodict.parse(xml)
    posts = db.Project
    result = posts.insert_one(my_dict)
    # print('One post: {0}'.format(result.inserted_id))


def retrieve_list_of_projects():
    client = MongoClient('localhost', 27017)
    # print(client)
    db = client.BEAT
    # print(db)

    projects = db.Project
    projectsList = projects.find()

    # print(projectsList)

    list_of_projects = []
    for item in projectsList:
        list_of_projects.append(item['Project']['Project_name']['#text'])
    return list_of_projects


def retrieve_selected_project(project_name):
    client = MongoClient('localhost', 27017)
    # print(client)
    db = client.pymongo_test
    # print(db)
    projects = db.posts
    projectsList = projects.find()

    for item in projectsList:
        if item['Project']['Project_name']['#text'] == project_name:
            print('************************************')
            print(item)
            return item


def delete_selected_project(nameofProject):
    client = MongoClient('localhost', 27017)
    db = client.pymongo_test
    projects = db.posts
    myquery = {"Project.Project_name.#text": nameofProject}
    projects.delete_one(myquery)

#holder element of where to place xml2
def xmlmerger(holder,xml1,xml2):
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    for element1 in xml1.findall(holder):
        element1.append(xml2)
    ET.dump(xml1)
    print(xml1)
    print("+++++++++++++++++++++++++++++++++++++++++++++++")

