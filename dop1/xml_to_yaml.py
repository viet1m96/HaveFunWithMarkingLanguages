import xmlplain

with open("./input.xml", encoding='utf-8') as infile:
  root = xmlplain.xml_to_obj(infile, strip_space=True, fold_dict=True)

with open("./output.yaml", "w", encoding='utf-8') as outfile:
  xmlplain.obj_to_yaml(root, outfile)