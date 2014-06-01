#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

def echo(sock):
    try:
        while True:
            data = sock.recv(1024) # 受信できるまでブロック
            if not data:
                break
            sock.sendall(data) # 送信できるまでブロック
    finally:
        sock.close()

def serve(addr):
    sock = socket.socket()
    sock.bind(addr); sock.listen(50)
    while True:
        conn, _ = sock.accept() # 
        echo(conn) #

if __name__ == '__main__':
    serve(('0.0.0.0', 4000))
