from pymongo import MongoClient
import xmltodict
import xml.etree.ElementTree as ET


# PROJECT TAB
class ProjectXmlManager():
    def __init__(self):
        self.projectPath = MongoClient('localhost', 27017).beat.Project # sets path to connect to DB
    
    def uploadXML(self, xml):
        my_dict = xmltodict.parse(xml) # parse XML into dictionary compatible with MongoDB
        self.projectPath.insert_one(my_dict)
        
    def retrieve_list_of_projects(self):
        projectsList = self.projectPath.find()
    
        list_of_projects = []
        for item in projectsList:
            try:
                list_of_projects.append(item['Project']['Project_name']['#text'])
            except:
                continue
    
        return list_of_projects
    
    def retrieve_selected_project(self, project_name):
        projectsList = self.projectPath.find()
    
        for item in projectsList:
            if item['Project']['Project_name']['#text'] == project_name:
                return item
            
    def delete_selected_project(self, nameofProject):
        myquery = {"Project.Project_name.#text": nameofProject}
        self.projectPath.delete_one(myquery)
    
    def update_proj_description(self, old_description, new_description):
        myquery = {"Project.projectDescription.#text": old_description}
        new_values = {"$set": {"Project.projectDescription.#text": new_description}}
        self.projectPath.update_one(myquery, new_values)
    
    def project_exists(self, new_project_name):
        projectsList = self.projectPath.find()
        for item in projectsList:
            if item['Project']['Project_name']['#text'] == new_project_name:
                return True
        return False

# Used for Analysis tab
class AnalysisXmlManager():
    def __init__(self):
#         self.poiDataSetPath = MongoClient('localhost', 27017).beat.pointOfInterestDataSet
        self.projectPath = MongoClient('localhost', 27017).beat.Project
    
    def uploadDataSet(self, xml):
        my_dict = xmltodict.parse(xml)
        self.projectPath.insert_one(my_dict)
         
# Used for Plugin Tab and Analysis Tab
class PluginXmlManager():
    def __init__(self):
        self.pluginPath = MongoClient('localhost', 27017).beat.Plugin
        self.systemPath = MongoClient('localhost', 27017).beat.System
    
    def uploadSystem(self, xml): # also on beatmain.py(*gonna duplicate in system xml manager)
        my_dict = xmltodict.parse(xml)
        self.systemPath.insert_one(my_dict)
        
    def delete_system(self):
        self.systemPath.drop()
        
    def is_system_empty(self):
        self.systemPath.find()
        list_of_projects = []
        for item in projectsList:
            list_of_projects.append(item['System'])
        if list_of_projects==[]:
            return True
        else:
            return False
        
    def retrieve_list_of_plugins(self): # also on  analysisTab.py
        pluginList = self.pluginPath.find()
        list_of_plugins = []
        for item in pluginList:
            list_of_plugins.append(item['Plugin']['Plugin_name']['#text'])
        return list_of_plugins
    
    def delete_selected_plugin(self, nameofplugin):
        myquery = {"Plugin.Plugin_name.#text": nameofplugin}
        self.pluginPath.delete_one(myquery)
    
    def retrieve_selected_plugin(self, plugin_name):
        pluginList = self.pluginPath.find()
        for item in pluginList:
            if item['Plugin']['Plugin_name']['#text'] == plugin_name:
                return item
        for item in projectsList:
            if item['Project']['BinaryFilePath']['#text'] == project_name:
                return item
        
    def uploadPlugin(self, xml):
        my_dict = xmltodict.parse(xml)
        self.pluginPath.insert_one(my_dict)
    
    def plugin_exists(self, new_plugin_name):
        pluginList = self.pluginPath.find()
        for item in pluginList:
            if item['Plugin']['Plugin_name']['#text'] == new_plugin_name:
                return True
        return False
    
    def update_plugin_description(self, old_description, new_description):
        myquery = {"Plugin.Plugin_Desc.#text": old_description}
        new_values = {"$set": {"Plugin.Plugin_Desc.#text": new_description}}
        self.pluginPath.update_one(myquery, new_values)
        
    # holder element of where to place xml2
    def xmlmerger(self, holder, xml, xml2):
        tree1=ET.parse(xml)
        tree2=ET.parse(xml2)
        xml2=tree2.getroot()
        for element1 in tree1.findall(holder):
            element1.append(xml2)
        return tree1
    
class SystemXmlManager():
    def __init__(self):
        self.pluginPath = MongoClient('localhost', 27017).beat.Plugin
    
    