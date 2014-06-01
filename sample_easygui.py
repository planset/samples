#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

#curdir = os.path.abspath(os.path.dirname(__file__))
#sys.path.insert(0, os.path.join(curdir, 'easygui-0.96.zip'))
sys.path.insert(0, 'easygui-0.96.zip')

from easygui import *

def msgbox1():
    msgbox("hello world!!")

def msgbox2():
    msgbox("hello python!", "easygui", ok_button="Bye!", image="./sample_easygui_image.png")

def msgbox3():
    msgbox("はろう", "easygui", ok_button="Bye!", image="./sample_easygui_image.png")

def show_input_window():
    msg="おまえはなにものだ？"
    title = "とい"
    fieldStrings = ["わたしは","ねんれいは","せいべつは","しゅみは"]
    fieldValues = multenterbox(msg, title, fieldStrings)
    for v in fieldValues:
        print v
    else:
        print 'cancel'

if __name__ == '__main__':
    msgbox1()
    msgbox2()
    msgbox3()
    show_input_window()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
