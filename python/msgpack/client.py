import msgpackrpc 
import sys
import time
import logging
from functools import wraps

RETRY_COUNT = 3
RETRY_WAIT_TIME = 10

logging.basicConfig(level=logging.DEBUG)

def retry_call(preretry_method):
    def _retry_call(func):
        @wraps(func)
        def __retry_call(*args, **kwargs):
            cnt = RETRY_COUNT - 1
            while cnt > 0:
                try:
                    return func(*args, **kwargs)
                except:
                    cnt -= 1
                    logging.debug("retry waiting...")
                    time.sleep(RETRY_WAIT_TIME)
                    logging.debug("do preretry_method")
                    preretry_method()
            return func(*args, **kwargs)
        return __retry_call
    return _retry_call

def pre_retry_call():
    global client
    client = msgpackrpc.Client(msgpackrpc.Address("localhost", 18800))

@retry_call(pre_retry_call)
def proc():
    result = client.call('sum', 1, 2, clientname)  # = > 3
    print result

clientname="noname"
if len(sys.argv) > 1:
    clientname=sys.argv[1]
client = msgpackrpc.Client(msgpackrpc.Address("localhost", 18800))

for i in xrange(100000):
    proc()


