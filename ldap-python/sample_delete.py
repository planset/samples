#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import ldap

from config import uri, dc, user_dn, user_pw


try:
    con = ldap.initialize(uri)
    con.bind_s(user_dn, user_pw)

    con.delete_s('uid=francis,ou=People,' + dc)

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



