#!/usr/bin/env python
# -*- coding: utf-8 -*-

def runserver_1(host, port):
    print 'run server 1'

def runserver_2(host, port=80):
    """こんなコマンドです
    
    options:
        -h HOST, --host=HOST  こっちは必須です。
        -p PORT, --port=PORT  こっちはデフォルトの値付きの任意引数です。
    """
    print 'run server 2 host={0}, port={1}'.format(host, port)

if __name__ == '__main__':
    import clime.now

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
