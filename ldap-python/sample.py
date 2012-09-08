#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import ldap

import ldap_helper
from config import uri, dc, user_dn, user_pw

try:
    con = ldap.initialize(uri)
    con.bind_s(user_dn, user_pw)

    base_dn = dc

    raw_results = con.search_s(base_dn, ldap.SCOPE_SUBTREE)

    results = ldap_helper.get_search_results(raw_results)
    for result in results:
        print result.pretty_print()
#    for result in results:
#        print result.to_ldif()


except ldap.LDAPError, e:
    if type(e.message) == dict:
        messages = [ "{title}: {message}\n".format(title=k, message=v)
                     for k,v in e.message.iteritems()]
        for message in messages:
            print message
    else:
        print e.message()
        sys.exit(1)

finally:
    if con:
        con.unbind()


