import sys
_stdin = open(sys.stdin.fileno(), 'r', encoding='sjis')
_stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8')

for line in _stdin:
    print('!!!', file=sys.__stdout__)
    print('???', file=sys.__stderr__)
    _stdout.write(line)
