def generateEndingTag(startingTag):
    ending_tag = "</"
    for char in startingTag:
        if char != '<' and char != '>':
            ending_tag += char
    ending_tag += '>'
    return ending_tag

def generateStartingTag(source_str, idx):
    starting_tag = ""
    while source_str[idx.get_value()] != '>':
        starting_tag += source_str[idx.get_value()]
        idx.increment()
    starting_tag += '>'
    idx.increment()
    return starting_tag

def generatingCurrentEndingTag(source_str, idx):
    theme_tag = "</"
    idx.increment(2)
    while source_str[idx.get_value()] != '>':
        theme_tag += source_str[idx.get_value()]
        idx.increment()
    theme_tag += '>'
    idx.increment()
    return theme_tag

def generatingContent(source_str, idx):
    content = ""
    while source_str[idx.get_value()] != '<':
        if source_str[idx.get_value()] != ' ' and source_str[idx.get_value()] != '\n':
            content += source_str[idx.get_value()]
        idx.increment()
    return content

def generatingRealTag(startingTag):
    real_tag = ""
    for i in range(1, len(startingTag) - 1):
        real_tag += startingTag[i]
    return real_tag