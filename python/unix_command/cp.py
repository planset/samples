#!/usr/bin/env python
# encoding: utf-8
"""
標準入出力を使用したファイルのコピー
"""

import sys

while True:
    try:
        c = sys.stdin.read(1)
    except Exception, e:
        sys.exit("read error")
        
    try:
        sys.stdout.write(c)
    except Exception, e:
        sys.exit("write error")
    
sys.exit(0)
