#!/usr/bin/env python
# -*- coding: utf-8

"""
ディレクトリ内の全てのファイルをリストする
"""
import sys, os

if len(sys.argv) != 2:
    sys.exit("a single argument (the directory name) is required")

try:
    filenames = os.listdir(sys.argv[1])
except OSError, e:
    sys.exit("can't open{0}".format(sys.argv[1]))

for filename in filenames:
    print filename

sys.exit(0)