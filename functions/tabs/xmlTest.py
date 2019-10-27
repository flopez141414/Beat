import xml.etree.ElementTree as ET
tree = ET.parse('practiceXml.xml')
root = tree.getroot()

#iterate on xml

for x in root.iter('PointOfInterest'):
    print(x.attrib)  # x.text

#modyfying XML
b2tf = root.find("./Project_name")
print(b2tf)
b2tf.text = "Back to the Future"
print(b2tf.attrib)
print('********************************')
print(ET.tostring(root, encoding='utf8').decode('utf8'))