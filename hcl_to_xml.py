import hcl2
import json
import sys
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def to_xml(data, parent=None):
    if parent is None:
        parent = Element('terraform')
    
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, list):
                for item in value:
                    child = SubElement(parent, key)
                    to_xml(item, child)
            else:
                child = SubElement(parent, key)
                to_xml(value, child)
    elif isinstance(data, list):
        for item in data:
            to_xml(item, parent)
    else:
        parent.text = str(data)
    
    return parent

def hcl_to_xml(hcl_file):
    with open(hcl_file, 'r') as f:
        hcl_data = hcl2.load(f)
    
    xml_root = to_xml(hcl_data)
    xml_str = minidom.parseString(tostring(xml_root)).toprettyxml(indent="  ")
    return xml_str

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hcl_to_xml.py <terraform_file.tf>")
        sys.exit(1)
    
    xml_output = hcl_to_xml(sys.argv[1])
    print(xml_output)
