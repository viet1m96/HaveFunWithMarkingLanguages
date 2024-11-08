import re

def parser(inp):
    yaml_data = "schedule:\n  para:\n"
    pattern = re.compile(r"<para>(.*?)</para>", re.DOTALL)
    for para in pattern.findall(inp):
        yaml_data += "    -\n"
        for field in ["Group", "Day", "Lesson", "Name", "Time", "Teacher", "Hall", "Place"]:
            match = re.search(f"<{field}>(.*?)</{field}>", para)
            if match:
                value = match.group(1)
                yaml_data += f"      {field}: '{value}'\n"
    return yaml_data

def process() :
    try:
        with open('./input.xml', 'r', encoding='utf-8') as infile:
            content = ''.join(infile.readlines()[1:])
        yaml_content = parser(content)

        with open('./output.yaml', 'w', encoding='utf-8') as outfile:
            outfile.write(yaml_content)

        print("Successfully converted XML to YAML")
    except Exception as e:
        print(e)

process()