#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from fabric.api import local, settings, abort, run, cd, env, sudo, roles, put, execute, \
                       runs_once, warn, show, get

from fabric.contrib.console import confirm
from fabric.contrib import files

#env.user = 'administrator'
#env.password = 'F-usac2626'
#env.hosts = ['administrator@localhost', 'igarashi@192.168.0.192']

env.roledefs = {
        #    'production': ['azureuser@shikkarifarm.com:54786'],
        'staging': ['azureuser@dev.shikkarifarm.com'],
        #'development': ['administrator@192.168.0.174'],
        #'test': ['azureuser@10.1.2.131'],
}


env.app_path = '/var/www/ams'
env.app_path_for_apache = '/var/www/ams/app'
env.admin_mail = 'info@f-usac.co.jp'


def production():
    env.environment = 'production'
    env.www_server_name = 'shikkarifarm.com'
    env.repository_host = 'dev.shikkarifarm.com'
    env.repository = 'ssh://%(repository_host)s/var/git/ams' % env

def staging():
    env.environment = 'staging'
    env.www_server_name = 'dev.shikkarifarm.com'
    env.repository_host = 'dev.shikkarifarm.com'
    env.repository = 'ssh://%(repository_host)s/var/git/ams' % env

def development():
    env.environment = 'development'
    env.www_server_name = 'dev.ams.f-usac.co.jp'
    env.repository_host = '192.168.0.192'
    env.repository = 'ssh://%(repository_host)s/var/dotnet2_git/ams' % env


def hello():
    print env.host


@runs_once
def _production_check():
    if "prod" in env.environment:
        if not confirm('Is it ok to deploy to production?', default=False):
            abort('Production deploy cancelled.')

def _git_pull():
    with cd(env.app_path):
        run('git pull origin master')

def exists(path):
    with settings(warn_only=True):
        return run('test -e %s' % path).succeeded

def exists_dir(path):
    with settings(warn_only=True):
        return run('test -d %s' % path).succeeded

def apache_graceful():
    sudo('/etc/init.d/apache2 graceful')


def switch_site(site_name):
    if site_name == 'ams':
        sudo('a2dissite ams_maintenance')
        sudo('a2ensite ams')
    elif site_name == 'ams_maintenance':
        sudo('a2dissite ams')
        sudo('a2ensite ams_maintenance')
    apache_graceful()



def _install_debian_packages():
    # apt-get でインストールできるアプリをインストール
    sudo('apt-get update')
    packages = []
    with open('packages/debian_packages.txt') as f:
        packages = f.read().strip().split('\n')

    for package in packages:
        if package == '' or package.startswith('#'):
            continue
        if package == 'mysql-server':
            sudo('DEBIAN_FRONTEND=noninteractive apt-get install -q -y mysql-server')
            sudo('mysqladmin -uroot password F-usac2626')
        else:
            sudo('apt-get install -y ' + package)

def _install_python_packages():
    # pipでインストール
    packages = []
    with open('packages/python_packages.txt') as f:
        packages = f.read().strip().split('\n')
    for package in packages:
        if package == '' or package.startswith('#'):
            continue
        sudo('pip install -U ' + package)

def _install_perl_packages():
    # cpanmでインストール
    packages = []
    with open('packages/perl_packages.txt') as f:
        packages = f.read().strip().split('\n')
    for package in packages:
        if package == '' or package.startswith('#'):
            continue
        sudo('cpanm ' + package)

def _setup_user_and_group():
    # ユーザーやグループの設定
    sudo('groupadd webadmin')
    sudo('gpasswd -a www-data webadmin')
    sudo('gpasswd -a azureuser webadmin')

def _setup_ams_files():
    sudo('mkdir -p ~/.ssh')
    put('keys/repository_key', '~/.ssh/id_rsa', mode=0700)
    put('keys/repository_key.pub', '~/.ssh/id_rsa.pub', mode=0700)
    #put('git-ssh.sh', '~/git-ssh.sh', mode=755)

    sudo('mkdir -p /var/www')
    sudo('chown -R azureuser:webadmin /var/www')
    sudo('find /var/www -type d | xargs chmod g+ws')

    run('ssh-keyscan -H %(repository_host)s >> .ssh/known_hosts' % env)
    with cd('/var/www'):
        run('git clone %(repository)s' % env)

    with cd(env.app_path):
        run('find . -name "*.cgi" | xargs chmod +x')

    # Install Kapp and dependencies
    with cd(env.app_path + '/app/lib'):
        run('tar zxf Kappa-0.18.tar.gz')
        with cd('Kappa-0.18'):
            sudo('cpanm --installdeps .')
            #sudo('make test')
            sudo('make install')


def _setup_ams_database():
    # setup database
    with cd(env.app_path):
        run('chmod +x migrate.py')
        #run('echo "drop database ams"| mysql -uroot -p')
        run('mysql -uroot -pF-usac2626 < db/create_database.sql')
        run('./migrate.py migrate 1')
        run('./migrate.py initial_data')
        run('./migrate.py migrate')

def _setup_ams_apache():
    # setup apache 
    #sudo('sed -i -e \'s/%(www_server_name)/hogehoge.com\' /etc/apache2/sites-available/ams')
    sudo('a2dissite default')
    with cd(env.app_path):
        for fn in ['ams', 'ams_maintenance']:
            source = os.path.join('conf', fn)
            dest = os.path.join('/etc/apache2/sites-available', fn)
            files.upload_template(source, dest, context=env, #mode=0755,
                                  use_sudo=True)


def setup():
    """農業管理システムに必要なサービスをインストールし、ウェブから閲覧できるようにする。"""
    _install_debian_packages()
    _install_python_packages()
    _install_perl_packages()

    _setup_user_and_group()

    _setup_ams_files()
    _setup_ams_database()
    _setup_ams_apache()

    # start site
    switch_site('ams')


def prepare_setup():
    put('~/.ssh/id_rsa.pub', 'deploy_base_id_rsa.pub')
    run('mkdir -p .ssh')
    run('cat deploy_base_id_rsa.pub >> .ssh/authorized_keys')


def migrate_database_to_latest_version():
    with cd(env.app_path):
        run('./migrate.py migrate 9999')

def update_apache_conf(process_count=15, thread_count=1):
    env.process_count = process_count
    env.thread_count = thread_count
    for fn in ['ams', 'ams_maintenance']:
        source = os.path.join('conf', fn)
        dest = os.path.join('/etc/apache2/sites-available', fn)
        files.upload_template(source, dest, context=env, mode=0755,
                              use_sudo=True)
    apache_graceful()


