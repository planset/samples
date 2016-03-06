#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator

def find_same_dict_from_dictlist(list_of_dict):
    """fnid same dict from list of dict
    
    >>> ds = [ {1:1, 2:2, 3:3}, \
               {1:2, 2:2, 3:3}, \
               {1:1, 2:2, 3:3}, \
             ]
    >>> find_same_dict_from_dictlist(ds)
    {1:1, 2:2, 3:3}
    """
    common_items = reduce(operator.__and__, 
            (d.viewitems() for d in list_of_dict))
    print common_items
    common_keys = [item[0] for item in common_items]
    print common_keys

ds = [ {1:1, 2:2, 3:3},
       {1:2, 2:2, 3:3},
       {1:1, 2:2, 3:3}
     ]
find_same_dict_from_dictlist(ds)

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags = (doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS))


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
