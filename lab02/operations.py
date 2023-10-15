def first_character(input_string):
    if input_string:
        return input_string[0]
    else:
        return ""

def first_two_characters(input_string):
    if len(input_string) >= 2:
        return input_string[:2]
    else:
        return ""

def all_characters_except_first_two(input_string):
    if len(input_string) >= 3:
        return input_string[2:]
    else:
        return ""

def penultimate_character(input_string):
    if len(input_string) >= 2:
        return input_string[-2]
    else:
        return ""

def last_three_characters(input_string):
    if len(input_string) >= 3:
        return input_string[-3:]
    else:
        return ""

def all_characters_in_even_positions(input_string):
    return input_string[0::2]

def merge_characters_and_duplicate(input_string):
    first_char = first_character(input_string)
    penultimate_char = penultimate_character(input_string)
    
    if not input_string:
        return ""
    
    result = (first_char + penultimate_char) * len(input_string)
    
    return result
