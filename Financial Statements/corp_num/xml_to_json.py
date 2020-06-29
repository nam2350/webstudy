# -*-coding: utf-8-*-
import json
import xmltodict
 
with open("CORPCODE.xml",'r') as f:
    xmlString = f.read()
 
print("xml input (CORPCODE.xml):")
print(xmlString)
 
jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
 
print("\nJSON output(output.json):")
print(jsonString)
 
with open("CORPCODE.json", 'w') as f:
    f.write(jsonString)