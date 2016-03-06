from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'mysql_engine':'InnoDB'}

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    fullname = Column(String(255))
    password = Column(String(255))
    images = relationship("Image", backref='users', cascade="all, delete, delete-orphan" )

    def __init__(self, name, fullname, password):
        """"""
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        """"""
        return "<User(%s)>" % self.name

class Image(Base):
    __tablename__ = 'images'
    __table_args__ = ((UniqueConstraint(Image.filepath)), {'mysql_engine':'InnoDB'})

    id = Column(Integer, primary_key=True)
    filename = Column(String(255))
    filepath = Column(String(255))
    filesize = Column(Integer)
    width = Column(Integer)
    height = Column(Integer)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User")

    def __init__(self, filename, owner):
        """"""
        self.filename = filename
        self.owner = owner

    def __repr__(self):
        """"""
        return "<Image(%s)>" % self.filename


