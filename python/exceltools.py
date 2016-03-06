#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string                                                                   

def base_n(number,base):                                                        
    """
    >>> base_n(0, 26)
    'A'
    >>> base_n(27, 26)
    'AB'
    """
    code = string.ascii_uppercase[:base]                                        
    return ("" if number<base else base_n(number//base-1,base)) + str(code[number%base])

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags = (doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS))

