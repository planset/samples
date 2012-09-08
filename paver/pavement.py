from paver.easy import *
import os

@task
def hello():
    """"""
    print 'hello'


@task
@consume_args
def hello(args):
    """"""
    print 'hello', args

@task
@cmdopts([
    ('foo', 'f', ' The foo'),
    ('bar=', 'b', 'Bar bar bar'),
    ])
def hello(options):
    """"""
    print 'hello', options.foo, options.bar


@task
def chdir():
    print 'cwd: ', os.getcwd()
    with pushd('/'):
        print 'cwd: ', os.getcwd()
    print 'cwd: ', os.getcwd()


