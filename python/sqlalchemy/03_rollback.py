from models import User
from session import session

print len(session.query(User).all())

session.add(User('hoge','hoge','hoge'))

print len(session.query(User).all())

session.rollback()

print len(session.query(User).all())



