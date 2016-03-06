#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess

def authenticate(fn):
    def wrapper(*args, **kwargs):
        euid = os.geteuid()
        if euid != 0:
            print 'This command requires privliged mode. Enter password..'
            os.execvp('sudo', ['sudo', 'python'] + sys.argv)
        fn(*args, **kwargs)
    return wrapper

@authenticate
def main(pid):
    dirpath = '/proc/{pid}/fd'.format(pid=pid)
    for fd_filepath in [ os.path.join(dirpath, filename) 
            for filename in os.listdir(dirpath)]:
        p = subprocess.Popen(['sudo', 'readlink', fd_filepath], stdout=subprocess.PIPE)
        out,res = p.communicate()
        print out


if __name__ == '__main__':
    import sys
    pid = sys.argv[1]
    main(pid)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

