#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

class DummyMacWinsound(object):
    SND_ASYNC = 0x01
    SND_NOWAIT = 0x10
    def PlaySound(self, filename, flags):
        os.system('afplay ' + filename + '&')

class DummyLinuxWinsound(object):
    SND_ASYNC = 0x01
    SND_NOWAIT = 0x10
    def PlaySound(self, filename, flags):
        os.system('aplay ' + filename + '&')

if os.name == 'posix':
    if os.uname()[0]:
        winsound = DummyMacWinsound()
    else:
        winsound = DummyLinuxWinsound()
else:
    import winsound

