#!/usr/bin/env python
# -*- coding: utf-8 -*-

from session import session
import models

# Userを追加
session.add_all([models.User('name' + str(i), 'fullname', 'password') for i in range(100)])
session.commit()

# 最初のUserにImageを追加
users = session.query(models.User).all()

user = users[0]
session.add_all([models.Image('image' + str(i), user) for i in range(10)])

for user in users[1:5]:
    session.add_all([models.Image('image' + str(i), user) for i in range(5)])

session.commit()

