from subprocess import Popen, PIPE
import json
import requests

iwlist = Popen('iwlist wlan0 scan'.split(), stdout=PIPE)
grep = Popen('grep Address:'.split(),
             stdin=iwlist.stdout, stdout=PIPE)
awk = Popen(['awk', '{print $5}'],
            stdin=grep.stdout, stdout=PIPE)
mac_address = awk.communicate()[0].splitlines()

query = json.dumps(
    {'version': '1.1.0',
     'host': 'maps.google.com',
     'request_address': True,
     'address_language': 'ja_JP',
     'wifi_towers': [
         {'mac_address': d,
          'signal_strength': 8,
          'age': 0,
          } for d in mac_address],
    }
)

r = requests.post('http://www.google.com/loc/json', query)
d = json.loads(r.content)
print json.dumps(d, ensure_ascii=False, indent=4)
