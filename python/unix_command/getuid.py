#!/usr/bin/env python
# encoding: utf-8
"""
getuid.py

Created by planset on 2011-03-09.
Copyright (c) 2011 Daisuke Igarashi. All rights reserved.
"""

import os

print "uid = %d, gid = %d(%s)" % (os.getuid(), os.getgid(), os.getgroups())

