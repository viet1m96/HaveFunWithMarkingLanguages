import time

from compulsory.xml_to_yaml import process
from dop3.xml_to_yaml import convert_xml_to_yaml
start_time = time.time()
for i in range(100):
    process()
end_time = time.time()
t1 = end_time - start_time

start_time = time.time()
for i in range(100):
    convert_xml_to_yaml("./input.xml", "./output.yaml")
end_time = time.time()
t2 = end_time - start_time

if t1 > t2:
    print("compulsory is longer than dop3")
elif t2 > t1:
    print("compulsory is shorter than dop3")
else:
    print("they equal")