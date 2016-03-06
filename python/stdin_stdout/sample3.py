import sys
import codecs

_stdin = codecs.getreader('sjis')(sys.stdin.buffer)
print(_stdin.read())
