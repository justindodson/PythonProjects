
# return index of space in single string
def find_string_space_index(text):
    index = 0
    for letter in text:
        if letter == ' ':
            return index
        index += 1
    return index


# return text with additional spaces cut out after last letter
def cut_string_spaces(text):
    index = 0
    for letter in text:
        if letter == ' ':
            text = text[:index]
        index += 1
    return text
