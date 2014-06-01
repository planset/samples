#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import socket
from contextlib import closing

import sys
import binascii

host = sys.argv[1]
port = int(sys.argv[2])
if len(sys.argv) >= 3:
    data = b'shinnippon-k.com' #binascii.a2b_uu(sys.argv[3])
else:
    data = b''

backlog = 10
bufsize = 4096

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with closing(sock):
        sock.bind((host, port))
        sock.listen(backlog)
        while True:
            conn, address = sock.accept()
            with closing(conn):
                msg = conn.recv(bufsize)
                print(msg)
                conn.send(msg)

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with closing(sock):
        sock.connect((host, port))
        sock.send(data)
        print(sock.recv(bufsize))

def main():
    client()
    
if __name__ == '__main__':
    main()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

