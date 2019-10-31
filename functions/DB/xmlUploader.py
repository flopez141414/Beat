from pymongo import MongoClient
import xmltodict
import pprint
import json


def uploadXML(xml):
    client = MongoClient('localhost', 27017)
    # print(client)
    db = client.pymongo_test
    # print(db)

    my_dict = xmltodict.parse(xml)
    posts = db.posts
    result = posts.insert_one(my_dict)
    # print('One post: {0}'.format(result.inserted_id))


def retrieve_list_of_projects():
    client = MongoClient('localhost', 27017)
    # print(client)
    db = client.pymongo_test
    # print(db)

    projects = db.posts
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
            return item


def delete_selected_project(nameofProject):
    client = MongoClient('localhost', 27017)
    db = client.pymongo_test
    projects = db.posts
    myquery = {"Project.Project_name.#text": nameofProject}
    projects.delete_one(myquery)
