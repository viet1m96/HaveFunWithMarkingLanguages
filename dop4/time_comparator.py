import time
import compulsory.xml_to_yaml
import dop1.xml_to_yaml
import dop2.xml_to_yaml
import dop3.xml_to_yaml

start_time = time.time()
for i in range(100):
    compulsory.xml_to_yaml.process()
end_time = time.time()
t1 = end_time - start_time

start_time = time.time()
for i in range(100):
    dop2.xml_to_yaml.process()
end_time = time.time()
t2 = end_time - start_time

start_time = time.time()
for i in range(100):
    dop1.xml_to_yaml.process()
end_time = time.time()
t3 = end_time - start_time

start_time = time.time()
for i in range(100):
    dop3.xml_to_yaml.convert_xml_to_yaml("./input.xml", "./output.yaml")
end_time = time.time()
t4 = end_time - start_time

t1 = ("t1", t1)
t2 = ("t2", t2)
t3 = ("t3", t3)
t4 = ("t4", t4)
all_times = [t1, t2, t3, t4]

sorted_times = sorted(all_times, key=lambda x: x[1])
print(sorted_times)