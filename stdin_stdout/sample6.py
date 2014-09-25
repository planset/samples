import sys
import codecs

_stdin = codecs.getreader('sjis')(sys.stdin.buffer)
_stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

for line in _stdin:
    print('!!!', file=sys.__stdout__)
    print('???', file=sys.__stderr__)
    _stdout.write(line)

