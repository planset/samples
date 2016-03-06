import re
from functools import partial

def sample_partial_sub():
    """ Sample of sub with partial
    
    >>> sample_partial_sub()
    'This is a .'
    """
    erase_hoge = partial(re.compile(r'hoge').sub, '')
    return erase_hoge('This is a hoge.')

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags = (doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS))




