from pymongo import MongoClient
import xmltodict
import pprint
import json

client = MongoClient('localhost', 27017)
print(client)

db = client.pymongo_test
print(db)


my_xml = """
<project>
  <name>PROJECT EXAMPLE</name>
  <description>THIS IS A TEST</description>
  <binaryPath>SAMPLE PATH // // </binaryPath>
  <binaryProperties>
    <os>LINUX</os>
    <binaryType>ELF</binaryType>
    <machine>AMD</machine>
    <class>ELF64</class>
    <bits>64</bits>
    <language>TRUE</language>
    <canary>FALSE</canary>
    <crypto>FALSE</crypto>
    <nx>TRUE</nx>
    <pic>TRUE</pic>
    <relocs>FALSE</relocs>
    <relro>FULL</relro>
    <stripped>TRUE</stripped>
  </binaryProperties>
</project>
"""

my_dict = xmltodict.parse(my_xml)

posts = db.posts

result = posts.insert_one(my_dict)
print('One post: {0}'.format(result.inserted_id))