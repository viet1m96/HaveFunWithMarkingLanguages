def traverse_nested_dict(d, indent=0):
    """
    Hàm đệ quy để duyệt qua một nested defaultdict(list) và in từng key-value.
    """
    # Kiểm tra nếu d là dictionary (hoặc defaultdict)
    if isinstance(d, dict):
        for key, value in d.items():
            # In key với dấu thụt đầu dòng
            print(" " * indent + f"Key: {key}")

            # Gọi lại hàm đệ quy cho value
            traverse_nested_dict(value, indent + 4)

    # Kiểm tra nếu d là list
    elif isinstance(d, list):
        for item in d:
            # Gọi lại hàm đệ quy cho từng phần tử trong list
            traverse_nested_dict(item, indent + 4)

    # Nếu là kiểu dữ liệu khác, in trực tiếp
    else:
        print(" " * indent + f"Value: {d}")


def dict_to_yaml(d, indent=0):
    result = ""
    if isinstance(d, dict):
        for key, value in d.items():
            result += " " * indent + "- " + str(key[0]) + ":\n"
            if isinstance(value, list) and len(value) == 1:
                result += " " * indent + str(key[0]) + ": " + str(value[0]) + "\n"
            result += dict_to_yaml(value, indent + 1)
    elif isinstance(d, list):
        for item in d:
            result += dict_to_yaml(item, indent + 1)
    else:

        result += " " * (indent + 1) + d + "\n"

    return result
