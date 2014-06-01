
# `contextlib – コンテキストマネージャユーティリティ - Python Module of the Week <http://ja.pymotw.com/2/contextlib/index.html>`_

class SampleContext(object):
    def __init__(self):
        print 'init'

    def __enter__(self):
        print 'enter'

    def __exit__(self, exc_type, exc_value, traceback):
        print 'exit'

def test1():
    with SampleContext():
        print 'do something'


class WithinContext(object):

    def __init__(self, context):
        print 'WithinContext.__init__(%s)' % context
        
    def do_something(self):
        print 'WithinContext.do_something()'

    def __del__(self):
        print 'WithinContext.__del__'
        

class Context(object):

    def __init__(self):
        print 'Context.__init__()'

    def __enter__(self):
        print 'Context.__enter__()'
        return WithinContext(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'Context.__exit__()'
    
def test2():
    with Context() as c:
        c.do_something()


import contextlib

@contextlib.contextmanager
def make_context():
    print '  entering'
    try:
        yield {}
    except RuntimeError, err:
        print '  ERROR:', err
    finally:
        print '  exiting'

def test3():
    print 'Normal:'
    with make_context() as value:
        print '  inside with statement:', value

    print
    print 'Handled error:'
    with make_context() as value:
        raise RuntimeError('showing example of handling an error')

    print
    print 'Unhandled error:'
    with make_context() as value:
        raise ValueError('this exception is not handled')


class DoSomething(object):
    def __init__(self, target):
        self.target = target
        print '__init__ : ' + self.target

    def __enter__(self):
        print '__enter__ : ' + self.target
        return self.target

    def __exit__(self, exc_type, exc_value, traceback):
        #self.target.close()
        print '__exit__ : ' + self.target


def test4():
    item = 'hoge'
    with DoSomething(item):
        print 'item = ' + item


if __name__ == '__main__':
    test1()
    test2()
    test4()
    test3()





