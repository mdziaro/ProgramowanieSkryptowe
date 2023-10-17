import sys

def grep(pattern, input_text, ignore_case=False, whole_word=False):
    lines = input_text.split('\n')
    result = []

    for line in lines:
        line_to_compare = line if not ignore_case else line.lower()

        words = line.split()

        for word in words:
            word_to_compare = word if not ignore_case else word.lower()

            if whole_word:
                if word_to_compare == pattern:
                    result.append(line)
                    break
            else:
                if pattern in word_to_compare:
                    result.append(line)
                    break

    return '\n'.join(result)
