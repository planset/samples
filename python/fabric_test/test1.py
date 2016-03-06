#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import local, settings, abort, run, cd, env, sudo, roles, put, execute, \
                       runs_once, warn, show, get

from fabric.contrib.console import confirm

#env.user = 'administrator'
#env.password = 'F-usac2626'
#env.hosts = ['administrator@localhost', 'igarashi@192.168.0.192']

env.roledefs = {
    'production': ['azureuser@shikkarifarm.com:54786'],
    'staging': ['azureuser@f-usac-report.cloudapp.net'],
    'dev': ['administrator@192.168.0.174'],
}


@runs_once
def _production_check():
    if "prod" in env.environment:
        if not confirm('Is it ok to deploy to production?', default=False):
            abort('Production deploy cancelled.')


def hello(name="world"):
    print('Hello %s!' % name)
    print env



@roles('production', 'staging', 'development')
def pull(rev=None):
    print 'hello'



# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
