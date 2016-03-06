from __future__ import print_function
import sys
import codecs

_stdin = codecs.getreader('sjis')(sys.stdin)
print(_stdin.read())
