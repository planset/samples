#!/usr/bin/env python
# encoding: utf-8
"""
低レベルファイルIOを使って、標準入力から標準出力にファイルをコピーする
"""

import sys
import os


STDIN_FILENO = 0
STDOUT_FILENO = 1

BUFSIZE = 8192

while True:
    try:
        buf = os.read(STDIN_FILENO, BUFSIZE)
    except Exception, e:
        sys.exit("read error")
    
    if not buf:
        break
    
    try:
        os.write(STDOUT_FILENO, buf)
    except Exception, e:
        sys.exit("write error")
    
sys.exit(0)

