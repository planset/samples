#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import (Column, Integer, String, 
                        ForeignKey, Boolean, DateTime)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'mysql_engine':'InnoDB'}

    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    first_name = Column(String(30), nullable=False, default='')
    last_name = Column(String(30), nullable=False, default='')
    email = Column(String(255), nullable=False, default='')
    password = Column(String(255), nullable=False, default='')
    is_staff = Column(Boolean(), nullable=False, default=False)
    is_active = Column(Boolean(), nullable=False, default=True)
    is_superuser = Column(Boolean(), nullable=False, default=False)
    last_login = Column(DateTime(), nullable=False, 
            default=datetime.datetime.now())
    date_joined = Column(DateTime(), nullable=False, 
            default=datetime.datetime.now())
    description = Column(String(1024), nullable=False, default='')

    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password

    def __repr__(self):
        """"""
        return "<User(%s)>" % self.username


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
