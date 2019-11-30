from pymongo import MongoClient
import xmltodict
import pprint
import json


# sets path to connect to DB
def connection_project_path():
    client = MongoClient('localhost', 27017)
    db = client.beat
    posts = db.Project
    return posts


def connection_poi_path():
    client = MongoClient('localhost', 27017)
    db = client.beat
    posts = db.pointOfInterestDataSet
    return posts


def connection_plugin_path():
    client = MongoClient('localhost', 27017)
    db = client.beat
    posts = db.Plugin
    return posts


def uploadXML(xml):
    my_dict = xmltodict.parse(xml)
    posts = connection_project_path()
    result = posts.insert_one(my_dict)


def uploadPlugin(xml):
    my_dict = xmltodict.parse(xml)
    posts = connection_plugin_path()
    result = posts.insert_one(my_dict)


def uploadPOI(xml):
    my_dict = xmltodict.parse(xml)
    posts = connection_poi_path()
    result = posts.insert_one(my_dict)


def retrieve_list_of_projects_plugin():
    projects = connection_plugin_path()
    projectsList = projects.find()
    list_of_projects = []
    for item in projectsList:
        list_of_projects.append(item['Project']['Project_name']['#text'])  # NOTE modify
    return list_of_projects


def retrievePoiInProject():
    poiFileConnection = connection_poi_path()
    listofPois = poiFileConnection.find()
    poiList = []
    for item in listofPois:
        poiList.append(item['pointOfInterestDataSet']['stringHolder']['stringPointOfInterest'])
    return poiList


def retrieve_list_of_projects():
    projects = connection_project_path()
    projectsList = projects.find()
    list_of_projects = []
    for item in projectsList:
        list_of_projects.append(item['Project']['Project_name']['#text'])
    return list_of_projects


def retrieve_selected_project(project_name):
    projects = connection_project_path()
    projectsList = projects.find()

    for item in projectsList:
        if item['Project']['Project_name']['#text'] == project_name:
            return item


def retrieve_selected_project_path(project_name):
    projects = connection_project_path()
    projectsList = projects.find()

    for item in projectsList:
        if item['Project']['BinaryFilePath']['#text'] == project_name:
            return item


def delete_selected_project(nameofProject):
    projects = connection_project_path()
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


def project_exists(new_project_name):
    projects = connection_project_path()
    projectsList = projects.find()

    for item in projectsList:
        if item['Project']['Project_name']['#text'] == new_project_name:
            return True
    return False
