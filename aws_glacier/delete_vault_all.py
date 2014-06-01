#!/usr/pkg/bin/python2.7

from boto.glacier.layer1 import Layer1
from config import AWSAccesskey,AWSSecretAccesskey, AWSregion, VaultName
import json

data={u'TreeHash': None, u'VaultARN': u'arn:aws:glacier:eu-west-1:714589037097:vaults/MyVault', u'ContentType': 'application/json', u'RequestId': 'JSwuhzZAE9RmrWXekDzVtrYiEefqBAL74RcFOxt5cV9fCEM', u'ContentRange': None, u'InventoryDate': u'2012-08-29T12:59:36Z', u'ArchiveList': [{u'ArchiveId': u'BoZ8uZxSG1-WvtLaTP0-xSKmeP7B_CiRY_Ru9gnlgNMyWuYjSEmgWy33KbVaYUJLv7TGi9LQeOx620zu7-cLTqcXWXqle9yL1wlGPkNc-sGvan1XHLRnXhMK0SBoF7WIXVkr07JYAA', u'ArchiveDescription': u'', u'CreationDate': u'2012-08-28T06:40:43Z', u'SHA256TreeHash': u'794ce120c6bf985c767969cfc02364b97f526fad4f0929a531c4014017465f51', u'Size': 7982}, {u'ArchiveId': u'3w4o-nAHudiUxek9A26R7pEfkaLvM52cAEnPX8pBMNICpTmqkfu4aPCfc6VJNAdMYEeYWLs9osQpIS9Mmfw5YtPG3vLNMXFwLzzzV43Uf-v1LptujuB0F2TdHjStUO7JTlMSTeNpwQ', u'ArchiveDescription': u'', u'CreationDate': u'2012-08-28T22:56:59Z', u'SHA256TreeHash': u'439a092d1de8d6c901e1130ada43fec944e675d5bb85b08bef2185dc864ee29e', u'Size': 4052928}]}

glacier_layer1 = Layer1(aws_access_key_id=AWSAccesskey, aws_secret_access_key=AWSSecretAccesskey, region_name=AWSregion)

for archive in data['ArchiveList']:
    glacier_layer1.delete_archive(VaultName, archive['ArchiveId'])
glacier_layer1.delete_vault(VaultName)

