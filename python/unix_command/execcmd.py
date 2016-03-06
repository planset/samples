#!/usr/bin/env python
# encoding: utf-8
"""
標準出力からコマンドを読み込み、実行する
"""

import sys
import os

while True:
    try:
        buf = raw_input(u"% ")
    except EOFError, e:
        break
        
    try:
        pid = os.fork()
    except Exception, e:
        sys.exit("fork error")
    
    if pid == 0:
        try:
            os.execlp(buf, buf)
        except Exception, e:
            print >>sys.stderr, "couldn't execute"
            sys.exit(127)
    
    try:
        os.waitpid(pid, 0)
    except Exception, e:
        sys.exit("waitpid error")




