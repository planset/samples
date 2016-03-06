import sys
import io

_stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='sjis')
print(_stdin.read())
