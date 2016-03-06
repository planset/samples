#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

class Person(object):
    def age():
        doc = "The age property."
        def fget(self):
            return self._age
        def fset(self, value):
            self._age = value
        def fdel(self):
            del self._age
        return locals()
    age = property(**age())

    def name():
        doc = "The name property."
        def fget(self):
            return self._name
        def fset(self, value):
            self._name = value
        def fdel(self):
            del self._name
        return locals()
    name = property(**name())

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def happy_birthday(self):
        self._age += 1

    def hello(self):
        print('Hello !! My name is {}.'.format(self._name))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
