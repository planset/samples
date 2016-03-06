# Include the Dropbox SDK libraries
from dropbox import client, rest, session

# Get your app key and secret from the Dropbox developer website
APP_KEY = 'e6lpdx1vtw8bc0p'
APP_SECRET = 'dg30b9zm1biajh3'

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'app_folder'

sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

request_token = sess.obtain_request_token()

url = sess.build_authorize_url(request_token)

# Make the user log in and authorize this token
print "url:", url
print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
raw_input()

# This will fail if the user didn't visit the above URL and hit 'Allow'
access_token = sess.obtain_access_token(request_token)





import pickle
with open('token', 'w')as f:
    pickle.dump(access_token, f)

client = client.DropboxClient(sess)
print "linked account:", client.account_info()

# upload file
#with open('sample.txt', 'r')as f:
#    response = client.put_file('/upload_test.txt', f)
#    print "uploaded:", response

# folder metadata
folder_metadata = client.metadata('/')
print "metadata:", folder_metadata

# download data
#with open('download_test.txt', 'w')as f:
#    f.write(client.get_file('/upload_test.txt').read())
#    #f.write(client.get_file('/upload_test.txt', rev='').read())







