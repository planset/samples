#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from person import Person

class TestPerson(object):
    @pytest.fixture
    def p(self):
        return Person('hoge', 11)

    def test_create(self, p):
        assert p.name == 'hoge'
        assert p.age == 11

    def test_birthday(self, p):
        p = Person('hoge', 11)
        p.happy_birthday()
        assert p.age == 10
        

if __name__ == '__main__':
    pytest.main()
