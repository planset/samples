#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
import _io
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
    if isinstance(fin, _io.TextIOWrapper) and fin.encoding != fin_encoding:
        fin = codecs.getreader(fin_encoding)(fin.detach())
    if isinstance(fout, _io.TextIOWrapper) and fout.encoding != fout_encoding:
        fout = codecs.getwriter(fout_encoding)(fout.detach())

    fout.write(fin.read())


def main():
    #func1(sys.stdin, sys.stdout)
    func2(sys.stdin, sys.stdout, fin_encoding='sjis', fout_encoding='utf-8')


if __name__ == '__main__':
    main()

