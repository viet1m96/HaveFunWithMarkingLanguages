from pprint import pprint

from compulsory.dictionary_to_yaml import dict_to_yaml
from compulsory.xml_to_dictionary import transform_to_dict


def process():
    workWithFiles("./input.xml", "./output.yaml")


def workWithFiles(source_file, destination_file):
    try:
        with open(source_file, "r") as infile:
            source_str = ''.join(infile.readlines()[1:])
        dicta = transform_to_dict(source_str)
        destination_str = dict_to_yaml(dicta)
        with open(destination_file, "w") as outfile:
            outfile.write(destination_str)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")

process()
