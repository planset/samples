#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import stdio
"""
**for python3**

stdin, stdoutを使ってパイプ処理ができるようなコマンドを作る場合、
sys.stdin, sys.stdoutを利用して処理する。

* 文字コードが同じであれば、そのまま使ってOK -> func1
* 文字コードが違う場合には、codecsを使って文字コードを切り替える。
  sample::
    
      cat sample.csv | stdin_process     

  このような場合、sample.csvがSJISだとすると、
  文字コードを指定しない場合には、文字化けする。
  -> func2
"""


def func1(fin, fout):
    fout.write(fin.read())


def func2(fin, fout, fin_encoding='UTF-8', fout_encoding='UTF-8'):
    fin = stdio.stdin_with_encoding(fin_encoding)
    fout = stdio.stdout_with_encoding(fout_encoding)
    for line in fin:
        print('line', file=sys.stdout)
        fout.write(line)
    """
> cat sample.csv|python2 sample_stdin_stdout.py
line
1, ほげほげ
line
2, ふがふが
> cat sample.csv|python3 sample_stdin_stdout.py
line
line
1, ほげほげ
2, ふがふが
    """

def func3():
    """
    for python3
    これが一番わかりやすくて、スッキリしていて、更に挙動もいい感じじゃない？
    """
    fin = open(sys.stdin.fileno(), 'r', encoding='sjis')
    fout = open(sys.stdout.fileno(), 'w', encoding='UTF-8')
    ferr = open(sys.stderr.fileno(), 'w', encoding='UTF-8')
    for line in fin:
        print('stdout', file=sys.stdout)
        print('stderr', file=sys.stderr)
        fout.write(line)
    """
> cat sample.csv|python2 sample_stdin_stdout.py
stdout
stderr
1, ほげほげ
stdout
stderr
2, ふがふが
    """



def main():
    #func1(sys.stdin, sys.stdout)
    func2(sys.stdin, sys.stdout, fin_encoding='sjis', fout_encoding='utf-8')
    #func3()



if __name__ == '__main__':
    main()

