import xml.etree.ElementTree as ET
tree= ET.parse('practiceXml.xml')
root= tree.getroot()
print(root)
print(root.tag)
print(root.attrib)
for child in root:
    print(child.tag,child.attrib)
    for child2 in child:
        print(child2.tag,child2.attrib)
    
