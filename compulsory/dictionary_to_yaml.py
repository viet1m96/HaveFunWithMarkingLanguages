def dict_to_yaml(d, indent=0):
    result = ""
    if isinstance(d, dict):
        for key, value in d.items():
            if isinstance(value, list) and len(value) == 1:
                result += " " * (indent + 2) + str(key[0]) + ": " + str(value[0]) + "\n"
                return result
            else:
                if str(key[1]) == "root":
                    result += " " * indent + str(key[0]) + ":\n"
                else:
                    result += " " * indent + "- " + str(key[0]) + ":\n"
            result += dict_to_yaml(value, indent + 1)
    elif isinstance(d, list):
        for item in d:
            result += dict_to_yaml(item, indent + 1)

    return result
