def grep(text, search_pattern, ignore_case=False, whole_words=False):
    import re
    
    flags = re.MULTILINE
    if ignore_case:
        flags |= re.IGNORECASE
    
    if whole_words:
        search_pattern = r'\b' + re.escape(search_pattern) + r'\b'
    
    matches = re.finditer(search_pattern, text, flags)
    result = [match.group() for match in matches]
    
    return '\n'.join(result)