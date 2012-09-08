try:
    from private import *
except:
    import getpass
    uri = 'ldap://localhost'
    dc = 'dc=domain,dc=com'
    user_dn = 'cn=admin,' + dc
    user_pw = getpass.getpass("Password for %s:" % user_dn)


