from pymongo import MongoClient
import xmltodict
import pprint
import json
import xml.etree.ElementTree as ET
import sys
sys.path.append("../xml")
sys.path.append("../windows")


def connection_system_path(): # Plugin and main dependencies
    client=MongoClient('localhost',27017)
    db=client.beat
    post=db.System
    return post

# PROJECT TAB
# sets path to connect to DB
def connection_project_path():
    client = MongoClient('localhost', 27017)
    db = client.beat
    posts = db.Project
    return posts

def uploadXML(xml):
    my_dict = xmltodict.parse(xml)
    posts = connection_project_path()
    result = posts.insert_one(my_dict)
    
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

# ANALYSIS TAB
# get connection to database
def connection_poi_path():
    client = MongoClient('localhost', 27017)
    db = client.beat
    posts = db.pointOfInterestDataSet
    return posts
def uploadDataSet(xml):
    client = MongoClient('localhost', 27017)
    db = client.beat
    my_dict = xmltodict.parse(xml)
    dataSet = db.dataSet
    result = dataSet.insert_one(my_dict)
    
def retrievePoiInProject():
    poiFileConnection = connection_poi_path()
    listofPois = poiFileConnection.find()
    poiList = []
    for item in listofPois:
        poiList.append(item['PointOfInterestDataSet']['stringHolder']['stringPointOfInterest'])
    return poiList

# PLUGIN TAB
# get connection to database
def connection_plugin_path():
    client = MongoClient('localhost', 27017)
    db = client.beat
    posts = db.Plugin
    return posts

def uploadSystem(xml): # also on beatmain.py
    my_dict = xmltodict.parse(xml)
    posts = connection_system_path()
    result = posts.insert_one(my_dict)
    
def retrieve_list_of_plugins(): # also on  analysisTab.py
    plugins = connection_plugin_path()
    pluginList = plugins.find()

    list_of_plugins = []
    for item in pluginList:
        list_of_plugins.append(item['Plugin']['Plugin_name']['#text'])

    return list_of_plugins

def retrieve_selected_plugin(plugin_name):
    plugin = connection_plugin_path()
    pluginList = plugin.find()

    for item in pluginList:
        if item['Plugin']['Plugin_name']['#text'] == plugin_name:
            return item

    for item in projectsList:
        if item['Project']['BinaryFilePath']['#text'] == project_name:
            return item
    
def uploadPlugin(xml):
    my_dict = xmltodict.parse(xml)
    posts = connection_plugin_path()
    result = posts.insert_one(my_dict)

def delete_system():
    system = connection_system_path()
    system.drop()

def delete_selected_plugin(nameofplugin):
    plugins = connection_plugin_path()
    myquery = {"Plugin.Plugin_name.#text": nameofplugin}
    plugins.delete_one(myquery)

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
    
# holder element of where to place xml2
def xmlmerger(holder, xml, xml2):
    tree1=ET.parse(xml)
    tree2=ET.parse(xml2)
    xml2=tree2.getroot()
    for element1 in tree1.findall(holder):
        element1.append(xml2)
    return tree1

# MAIN
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
