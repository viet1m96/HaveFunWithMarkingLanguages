import xml.etree.ElementTree as ET
import yaml


def xml_to_dict(element):
    data = {}
    if element.text and element.text.strip():
        data['#text'] = element.text.strip()
    for key, value in element.attrib.items():
        data[f"@{key}"] = value
    for child in element:
        child_data = xml_to_dict(child)
        if child.tag in data:
            if type(data[child.tag]) is list:
                data[child.tag].append(child_data)
            else:
                data[child.tag] = [data[child.tag], child_data]
        else:
            data[child.tag] = child_data
    return data


def convert_xml_to_yaml(xml_file, yaml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data_dict = {root.tag: xml_to_dict(root)}

    with open(yaml_file, 'w') as f:
        yaml.dump(data_dict, f, default_flow_style=False, allow_unicode=True)


convert_xml_to_yaml("input.xml", "output.yaml")
