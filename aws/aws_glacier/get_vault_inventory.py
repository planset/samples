#!/usr/pkg/bin/python2.7

from boto.glacier.layer1 import Layer1

import sys, os
#sys.path.append(os.path.join(os.path.dirname(__file__), 'boto'))

from config import AWSAccesskey,AWSSecretAccesskey, AWSregion, VaultName

print AWSregion
print VaultName

glacier_layer1 = Layer1(aws_access_key_id=AWSAccesskey, aws_secret_access_key=AWSSecretAccesskey, region_name=AWSregion)


print("operation starting...");

job_id = glacier_layer1.initiate_job(VaultName, {"Description":"inventory-job", "Type":"inventory-retrieval", "Format":"JSON"})

print("inventory job id: %s"%(job_id,));

print("Operation complete.")



