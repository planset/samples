#!/usr/pkg/bin/python2.7


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'boto'))

from glacier import GlacierConnection
from glacier import GlacierWriter

from config import AWSAccesskey,AWSSecretAccesskey, AWSregion, VaultName

f = open('./glacier.py','r')
putsdata = f.read()
f.close()

glacierconn = GlacierConnection(AWSAccesskey, AWSSecretAccesskey, AWSregion)
writer = GlacierWriter(glacierconn, VaultName)
writer.write(putsdata)
writer.close()
print writer.get_archive_id()



