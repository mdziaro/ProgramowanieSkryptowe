import re

def grep(text, pattern, ignore_case=False, whole_word=False):
    ignore_case |= re.IGNORECASE
    if whole_word:
        pattern = r'\b{}\b'.format(re.escape(pattern))
    regex = re.compile(pattern, flags)
    lines = text.split('\n')
    result = []
    for line in lines:
        if regex.search(line):
            result.append(line)
    return '\n'.join(result)
