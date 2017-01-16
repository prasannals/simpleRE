def match(text, pattern, limit = -1):
    """
    Matches all or first "limit" number of occurances of the specified pattern in the provided text
    :param text: A String of characters. This is the text in which we want to find the pattern.
    :param pattern: The pattern to look for. Expected to be a regular expression.
    :param limit: The number of occurances of the pattern to be returned. If specified, the method returns the first
    "limit" number of occurances of the pattern in the text
    :return: A list of matching strings and their starting and ending index values in the format
    (matching_text, start_index, end_index)
    """