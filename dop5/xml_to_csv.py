import xml.etree.ElementTree as ET
import csv

def xml_to_csv(xml_path, csv_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    first_record = root[0]
    headers = [field.tag for field in first_record]

    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        for record in root:
            row_data = [record.find(field).text if record.find(field) is not None else '' for field in headers]
            writer.writerow(row_data)
xml_to_csv("./input.xml", "./output.csv")