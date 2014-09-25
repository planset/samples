import sys
import io

_stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='sjis')
_stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for line in _stdin:
    print('!!!', file=sys.__stdout__)
    print('???', file=sys.__stderr__)
    _stdout.write(line)
    _stdout.flush()

