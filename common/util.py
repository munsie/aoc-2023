def trim(s: str):
    '''
    Removes all extra whitespace, along with leading and trailing whitespace from the string.

    Args:
        s: string to remove whitespace from

    Returns:
        trim: string with extra whitespace removed.
    '''
    return ' '.join(s.split())

def int_list_from_string(s: str, delimiter=' '):
    '''
    Returns a list of integer values by splitting a string with the specified delimiter.

    Args:
        s: the string containing the integer values
        delimiter: the delimiter to seperate the string with

    Returns:
        int_list_from_string: list of integer values
    '''
    return [int(i) for i in s.split(delimiter)]
