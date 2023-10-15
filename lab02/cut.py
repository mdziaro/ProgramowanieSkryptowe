def cut(text, delimiter, field):
    lines = text.split('\n')
    result = []
    for line in lines:
        parts = line.split(delimiter)
        if field <= len(parts):
            result.append(parts[field - 1])
        else:
            result.append('')
    return '\n'.join(result)
