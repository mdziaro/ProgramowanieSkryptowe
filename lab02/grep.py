import sys

def grep(pattern, input_text, ignore_case=False, whole_word=False):
    lines = input_text.split('\n')
    result = []

    for line in lines:
        if ignore_case:
            line = line.lower()

        words = line.split()

        for word in words:
            if whole_word:
                if word == pattern:
                    result.append(line)
                    break
            else:
                if pattern in word:
                    result.append(line)
                    break
