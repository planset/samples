#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import local, settings, abort, run, cd, env, sudo, roles, put, execute, \
                       runs_once, warn, show, get

from fabric.contrib.console import confirm

env.user = 'administrator'
env.password = 'F-usac2626'
env.hosts = ['administrator@localhost', 'igarashi@192.168.0.192']

env.roledefs = {
    'production': ['azureuser@shikkarifarm.com:54786'],
    'staging': ['azureuser@f-usac-report.cloudapp.net'],
    'dev': ['igarashi@192.168.0.192', 'administrator@192.168.0.174'],
}


@runs_once
def _production_check():
    if "prod" in env.environment:
        if not confirm('Is it ok to deploy to production?', default=False):
            abort('Production deploy cancelled.')


def hello(name="world"):
    print('Hello %s!' % name)


def test():
    with settings(warn_only=True):
        result = local('./manage.py test my_app', capture=True)
    if result.failed and not confirm('Tests failed. Continue anyway>'):
        abort('Aborting at user request')

def commit():
    local(' git add -p && git commit')

def push():
    local('git push')

def prepare_deploy():
    test()
    commit()
    push()


def exists(path):
    with settings(warn_only=True):
        return run('test -e %s' % path).succeeded

def exists_dir(path):
    with settings(warn_only=True):
        return run('test -d %s' % path).succeeded

def deploy():
    code_dir = '/home/administrator/fabric_test/kss'

    with settings(warn_only=True):
        if run('test -d %s' % code_dir).failed:
            run('git clone ssh://igarashi@192.168.0.192/var/dotnet2_git/kss %s' % code_dir)

    with cd(code_dir):
        run('ls')
        sudo('ls')

def print_env():
    print env


def uname():
    run('uname -a')


@roles('staging')
def upload(project):
    items_string = local('ls', capture=True)
    items = items_string.split('\n')
    run('ls')

    tmp_path = 'hogehoge'
    if not exists_dir(tmp_path):
        run('mkdir %s' % tmp_path)

    with cd(tmp_path):
        put(items[0], items[0])
        run('ls')

    execute(uname, roles=['staging'])


def _git_pull():
    with cd(env.app_path):
        run('git pull origin master')


@roles('production', 'staging', 'development')
def pull(rev=None):
    _git_pull()




# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
