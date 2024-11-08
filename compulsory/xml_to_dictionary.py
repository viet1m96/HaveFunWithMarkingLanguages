from collections import defaultdict
from compulsory.generators import *
from Integer import IntegerWrapper


def nested_dict():
    return defaultdict(list)

#TREE
def xml_to_dict(tags, root, tails, source_str, idx):
    dicta = nested_dict()
    if root is None:
        root_tag = generateStartingTag(source_str, idx)
        end_root_tag = generateEndingTag(root_tag)
        root_tag = generatingRealTag(root_tag)
        tails.append(end_root_tag)
        tags[root_tag] = "root"
        root = (root_tag, tags.get(root_tag))

    while idx.get_value() < len(source_str):
        if source_str[idx.get_value()] == '<':
            if source_str[idx.get_value() + 1] != '/':
                starting_tag = generateStartingTag(source_str, idx)
                ending_tag = generateEndingTag(starting_tag)
                starting_tag = generatingRealTag(starting_tag)
                tails.append(ending_tag)
                if tags.get(starting_tag) is None:
                    tags[starting_tag] = 0
                else:
                    tags[starting_tag] += 1
                dicta[root].append(xml_to_dict(tags, (starting_tag, tags.get(starting_tag)), tails, source_str, idx))
            else:
                current_ending_tag = generatingCurrentEndingTag(source_str, idx)
                if current_ending_tag == tails[-1]:
                    tails.pop()
                    return dicta
        else:
            content = generatingContent(source_str, idx)
            if content != "":
                dicta[root].append(content)

    return dicta


def transform_to_dict(source_str):
    tags = {}
    idx = IntegerWrapper()
    tails = []
    root = None
    return xml_to_dict(tags, root, tails, source_str, idx)
