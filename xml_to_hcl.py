import sys
import xml.etree.ElementTree as ET

def process_attributes(element, indent):
    hcl = ""
    ind = "  " * indent
    
    for child in element:
        if child.text and child.text.strip() and not list(child):
            hcl += f'{ind}{child.tag} = "{child.text.strip()}"\n'
        else:
            content = process_attributes(child, indent + 1)
            hcl += f'{ind}{child.tag} {{\n{content}{ind}}}\n'
    
    return hcl

def xml_to_hcl(element, indent=0):
    hcl = ""
    ind = "  " * indent
    
    for child in element:
        block_type = child.tag
        
        # Special case: output, variable, locals (only have name, no type)
        if block_type in ['output', 'variable', 'locals', 'terraform']:
            for name_elem in child:
                name = name_elem.tag
                content = process_attributes(name_elem, indent + 1)
                hcl += f'{ind}{block_type} "{name}" {{\n{content}{ind}}}\n'
        # Standard case: resource, data, module (have type and name)
        elif len(child) == 1:
            type_elem = list(child)[0]
            resource_type = type_elem.tag
            
            for name_elem in type_elem:
                name = name_elem.tag
                content = process_attributes(name_elem, indent + 1)
                hcl += f'{ind}{block_type} "{resource_type}" "{name}" {{\n{content}{ind}}}\n'
        else:
            hcl += xml_to_hcl(child, indent)
    
    return hcl

def convert_xml_to_hcl(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return xml_to_hcl(root)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python xml_to_hcl.py <terraform.xml>")
        sys.exit(1)
    
    hcl_output = convert_xml_to_hcl(sys.argv[1])
    print(hcl_output)
