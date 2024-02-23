import xml.etree.ElementTree as ET
import json

# Load and parse the XML file
xml_file = 'your_xml_file.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

# Convert the XML data to a dictionary
def xml_to_dict(element):
    result = {}
    for child in element:
        if child:
            child_data = xml_to_dict(child)
            if child.tag in result:
                if type(result[child.tag]) is list:
                    result[child.tag].append(child_data)
                else:
                    result[child.tag] = [result[child.tag], child_data]
            else:
                result[child.tag] = child_data
        else:
            result[child.tag] = child.text
    return result

xml_data = xml_to_dict(root)

# Convert the dictionary to JSON
json_data = json.dumps(xml_data, indent=2)

# Save the JSON data to a file
json_file = 'your_converted_file.json'
with open(json_file, 'w') as f:
    f.write(json_data)

print(f"Conversion completed. JSON data saved to {json_file}")
