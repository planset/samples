# -*- coding: utf-8 -*-

# Include the Dropbox SDK libraries
from dropbox import client, rest, session
import os

# Get your app key and secret from the Dropbox developer website
APP_KEY = 'e6lpdx1vtw8bc0p'
APP_SECRET = 'dg30b9zm1biajh3'

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'app_folder'

sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

import simplejson as json
with open('token','r')as f:
    access_token = json.load(f, encoding='utf-8')
    
sess.set_token(access_token["key"].encode(), access_token[u"secret"].encode())

client = client.DropboxClient(sess)
#print "linked account:", client.account_info()

# folder metadata
folder_metadata = client.metadata('/')
#print "metadata:", folder_metadata

for content in folder_metadata["contents"]:
    print "%s(%d)" % (content["path"], int(content["bytes"]))

