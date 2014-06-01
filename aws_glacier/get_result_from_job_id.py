from boto.glacier.layer1 import Layer1
from boto.glacier.vault import Vault
from boto.glacier.job import Job
import sys
import os.path
import json
 
access_key_id = "..."
secret_key = "..."
target_vault_name = '...'
 
if(len(sys.argv) < 2):
    jobid = None
else:
    jobid = sys.argv[1]
 
from config import AWSAccesskey,AWSSecretAccesskey, AWSregion, VaultName

glacier_layer1 = Layer1(aws_access_key_id=AWSAccesskey, aws_secret_access_key=AWSSecretAccesskey, region_name=AWSregion)
 
print("operation starting...");
 
if(jobid != None):
    print glacier_layer1.get_job_output(VaultName, jobid)
else:
    print glacier_layer1.list_jobs(VaultName, completed=False)
 
     
print("Operation complete.")
