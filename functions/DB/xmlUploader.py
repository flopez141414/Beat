from pymongo import MongoClient
import xmltodict
import pprint
import json
import xml.etree.ElementTree as ET
import sys
sys.path.append("../xml")
sys.path.append("../windows")

# sets path to connect to DB
def connection_project_path():
    client = MongoClient('localhost', 27017)
    db = client.beat
    posts = db.Project
    return posts

def connection_system_path():
    client=MongoClient('localhost',27017)
    db=client.beat
    post=db.System
    return post

def connection_poi_path():
    client = MongoClient('localhost', 27017)
    db = client.beat
    posts = db.pointOfInterestDataSet
    return posts

def connection_poi_in_project_path(projectName):
    client= MongoClient('localhost',27017)
    db=client.beat
    project=db[projectName]['hello']
    return project

def retrieveSpecificProject(name):
    client=MongoClient('localhost',27017)
    db = client.beat
    projectsList = db.find(name)
    list_of_projects = []
    for item in projectsList:
        try:
            if name == item['Project']['Project_name']['#text']:
                list_of_projects.append(item)
        except:
            continue
    return list_of_projects

def connection_plugin_path():
    client = MongoClient('localhost', 27017)
    db = client.beat
    posts = db.Plugin
    return posts

def uploadSystem(xml):
    my_dict = xmltodict.parse(xml)
    posts = connection_system_path()
    result = posts.insert_one(my_dict)
    
def uploadXML(xml):
    my_dict = xmltodict.parse(xml)
    posts = connection_project_path()
    result = posts.insert_one(my_dict)

def uploadDataSet(xml):
    client = MongoClient('localhost', 27017)
    db = client.beat
    my_dict = xmltodict.parse(xml)
    dataSet = db.dataSet
    result = dataSet.insert_one(my_dict)

def uploadPlugin(xml):
    my_dict = xmltodict.parse(xml)
    posts = connection_plugin_path()
    result = posts.insert_one(my_dict)

def retrievePoiInProject():
    poiFileConnection = connection_poi_path()
    listofPois = poiFileConnection.find()
    poiList = []
    for item in listofPois:
        poiList.append(item['PointOfInterestDataSet']['stringHolder']['stringPointOfInterest'])
    return poiList

def retrieveSpecificProject(name):
    projects = connection_project_path()
    projectsList = projects.find()
    list_of_projects = []
    for item in projectsList:
        if name == item['Project']['Project_name']['#text']:
            list_of_projects.append(item)
    return list_of_projects

def retrieve_list_of_plugins():
    plugins = connection_plugin_path()
    pluginList = plugins.find()

    list_of_plugins = []
    for item in pluginList:
        list_of_plugins.append(item['Plugin']['Plugin_name']['#text'])

    return list_of_plugins

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
    
def retrieve_list_of_projects():
    projects = connection_project_path()
    projectsList = projects.find()

    list_of_projects = []
    for item in projectsList:
        try:
            list_of_projects.append(item['Project']['Project_name']['#text'])
        except:
            continue

    return list_of_projects

def retrieve_selected_project(project_name):
    projects = connection_project_path()
    projectsList = projects.find()

    for item in projectsList:
        if item['Project']['Project_name']['#text'] == project_name:
            return item

def retrieve_selected_plugin(plugin_name):
    plugin = connection_plugin_path()
    pluginList = plugin.find()

    for item in pluginList:
        if item['Plugin']['Plugin_name']['#text'] == plugin_name:
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

def update_proj_description(old_description, new_description):
    projects = connection_project_path()
    myquery = {"Project.projectDescription.#text": old_description}
    new_values = {"$set": {"Project.projectDescription.#text": new_description}}
    projects.update_one(myquery, new_values)

def project_exists(new_project_name):
    projects = connection_project_path()
    projectsList = projects.find()
    for item in projectsList:
        if item['Project']['Project_name']['#text'] == new_project_name:
            return True
    return False

    # holder element of where to place xml2
def xmlmerger(holder, xml, xml2):
    tree1=ET.parse(xml)
    tree2=ET.parse(xml2)
    xml2=tree2.getroot()
    for element1 in tree1.findall(holder):
        element1.append(xml2)
    return tree1

def xmlmergerByAddress(holder, xml1, xml2):
    tree = ET.parse(xml1)
    xml1 = tree.getroot()
    tree = ET.parse(xml2)
    xml2 = tree.getroot()
    for element1 in xml1.findall(holder):
        element1.append(xml2)
    xml3=ET.dump(xml1)
    return xml3

def uploadDataSet(xml):
    client = MongoClient('localhost', 27017)
    db = client.beat
    my_dict = xmltodict.parse(xml)
    dataSet = db.Project
    result = dataSet.insert_one(my_dict)
    
def delete_system():
    system = connection_system_path()
    system.drop()
    
def delete_selected_plugin(nameofplugin):
    plugins = connection_plugin_path()
    myquery = {"Plugin.Plugin_name.#text": nameofplugin}
    plugins.delete_one(myquery)

def update_proj_description(old_description, new_description):
    projects = connection_project_path()
    myquery = {"Project.projectDescription.#text": old_description}
    new_values = {"$set": {"Project.projectDescription.#text": new_description}}
    projects.update_one(myquery, new_values)

def project_exists(new_project_name):
    projects = connection_project_path()
    projectsList = projects.find()
    for item in projectsList:
        if item['Project']['Project_name']['#text'] == new_project_name:
            return True
    return False

def plugin_exists(new_plugin_name):
    plugins = connection_plugin_path()
    pluginList = plugins.find()
    for item in pluginList:
        if item['Plugin']['Plugin_name']['#text'] == new_plugin_name:
            return True
    return False

def update_plugin_description(old_description, new_description):
    plugins = connection_plugin_path()
    myquery = {"Plugin.Plugin_Desc.#text": old_description}
    new_values = {"$set": {"Plugin.Plugin_Desc.#text": new_description}}
    plugins.update_one(myquery, new_values)
    
def updateCurrentProject(currentProjectID):
    client = MongoClient('localhost',27017)
    beatDatabase = client.beat
    projectCollection = beatDatabase.Project
    project = projectCollection.find({'_id': currentProjectID})
    return project