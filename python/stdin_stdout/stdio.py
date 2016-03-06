# -*- coding: utf-8 -*-
import sys
import codecs
import io

def __reopen_with_encoding(f, encoding, getfunc):
    if isinstance(f, io.IOBase):
        # python3 
        if isinstance(f, io.TextIOWrapper) and f.encoding != encoding:
            # python3 text mode
            f = io.TextIOWrapper(f.buffer, encoding=encoding)
    else:
        # python2
        if isinstance(f, file) and f.encoding != encoding:
            f = getfunc(encoding)(f)
    return f

def stdin_original():
    return sys.__stdin__

def stdout_original():
    return sys.__stdout__

def stdin_with_encoding(encoding):
    return __reopen_with_encoding(sys.stdin, encoding, codecs.getreader)

def stdout_with_encoding(encoding):
    return __reopen_with_encoding(sys.stdout, encoding, codecs.getwriter)

def stdin(encoding='UTF-8'):
    return stdin_with_encoding(sys.stdin, encoding)

def stdout(encoding='UTF-8'):
    return stdout_with_encoding(sys.stdout, encoding)

