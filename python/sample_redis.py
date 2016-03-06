import redis

r = redis.Redis(host='10.37.129.31', port=6379, db=0)


def setdata():
    r.set('key', 'value')

def setlist():
    r.delete('list')
    r.lpush('list', 3)
    r.lpush('list', 2)
    r.lpush('list', 1)

    r.rpush('list', 4)
    r.rpush('list', 5)
    r.rpush('list', 6)
    
def renamelist():
    tempkey = 'templist'
    r.delete(tempkey)
    r.rpush(tempkey, 'hoge')
    r.rpush(tempkey, [1,2,3])
    r.rpush(tempkey, {'foo':'bar'})
    r.rename(tempkey, 'list')

def setset():
    r.sadd('tag:sing', 1)
    r.sadd('tag:sing', 3)
    r.sadd('tag:sing', 4)
    r.sadd('tag:sing', 5)
    r.sadd('tag:dance', 1)
    r.sadd('tag:dance', 2)
    r.sadd('tag:dance', 4)
    r.sadd('tag:dance', 5)

    r.srem('tag:dance', 2)
    r.sadd('tag:exclude', 4)

def getdata():
    print r.get('key')

    print r.llen('list')
    rs = r.lrange('list', 0, -1)
    for v in rs:
        print v,
    print 

    rs = r.sort('list', desc=True)
    for v in rs:
        print v,
    print 

    print r.smembers('tag:sing')
    print r.smembers('tag:dance')
    r.sinterstore('result1', 'tag:sing', 'tag:dance')
    r.sdiffstore('result2', 'result1', 'tag:exclude')
    rs = r.sort('result2', desc=True, by='access_count:*')
    for v in rs:
        print v,
    print 

def pipeline():
    r.set('bing', 'baz')
    pipe = r.pipeline(transaction=True)
    pipe.set('tran', 'tran1') # not execute here
    print pipe.get('tran')    # not execute here
    print pipe.get('bing')    # not execute here
    print pipe.execute()      # execute all, and returing a list of responses 
    print pipe.set('tran', 'tran1').get('tran').get('bing').execute() 

def pipeline2():
    r.set('bing', 'baz')
    pipe = r.pipeline(transaction=False)
    pipe.set('tran', 'tran1') # not execute here
    print pipe.get('tran')    # not execute here
    print pipe.get('bing')    # not execute here
    print pipe.execute()      # execute all, and returing a list of responses 

def watch():
    r.delete('OUR-SEQUENCE-KEY')
    #r.set('OUR-SEQUENCE-KEY', 0)
    with r.pipeline() as pipe:
        while 1:
            try:
                pipe.watch('OUR-SEQUENCE-KEY')
                current_value = pipe.get('OUR-SEQUENCE-KEY')
                next_value = int(current_value) + 1
                pipe.multi()
                pipe.set('OUR-SEQUENCE-KEY', next_value)
                pipe.execute()
                break
            except redis.WatchError:
                continue
            finally:
                pipe.reset()

watch()



setdata()
setlist()
setset()
getdata()

print '-' * 79

renamelist()
getdata()

print '-' * 79

pipeline()

print '-' * 79

pipeline2()


