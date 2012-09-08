# -*- coding: utf-8 -*-
from models import User, Image
from session import session

# UserとImageを追加する。
testuser = User('test_cascade', '', '')
testimage = Image('image name', testuser)

session.add(testuser)
session.add(testimage)
session.commit()

# 追加されているか確認
user = session.query(User).filter(User.name=='test_cascade').first()
image = session.query(Image).filter(Image.filename=='image name').first()
print user.name
print image.filename

# Userを削除する。Imageは直接削除しない。
session.delete(user)
session.commit()

# UserもImageも削除されていることを確認
user = session.query(User).filter(User.name=='test_cascade').first()
image = session.query(Image).filter(Image.filename=='image name').first()
print user
print image


