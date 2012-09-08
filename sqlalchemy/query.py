# -*- coding: utf-8 -*-
from sqlalchemy import and_

from models import User, Image
from session import session

def hr():
    print '=' * 79

def header(function_name):
    print '{name}'.format(name=function_name)
    hr()

def footer():
    print ''

def q_all():
    for row in session.query(User).all()[1:3]:
        print row.name

def q_filter_in():
    for row in session.query(User).filter(
            User.name.in_(['name'+str(i) for i in range(5)])
            ).all():
        print row.name

def q_filter_eq():
    for row in session.query(User).filter(User.name == 'name1').all():
        print row.name

def q_filter_like():
    for row in session.query(User).filter(User.name.like('%2%')).all():
        print row.name

def q_filter_eq_and():
    for row in session.query(Image).filter(and_(not Image.owner is None, Image.filename == 'image2')).all():
        print row.filename
        
def q_filter_join():
    for user, image in session.query(User, Image) \
                .filter(User.name == 'name0') \
                .filter(Image.filename == 'image3') \
                .all():
        print image.filename

def q_filter_outerjoin():
    for user, image in session.query(User, Image) \
                .outerjoin(Image, User.images) \
                .all()[25:35]:
        if image:
            print image.filename
        else:
            print 'Image is None'

def q_get():
    user = session.query(User).get(1)
    print user.name

def q_group_by():
    from sqlalchemy.sql import func
    q = session.query(User.name, func.count('*').label('image_count')).join(Image, User.images).group_by(User.name)
    for user in q.all():
        print user.name ,':', user.image_count

def q_subquery():
    stmt = session.query(User).filter(User.name == 'name1').subquery()
    for user in session.query(stmt).all():
        print user.name

def q_select_images_relation():
    for row in session.query(Image).all()[0:1]:
        print row.filename, '\'s owner is', row.owner.name

def q_select_users_relation():
    user = session.query(User).first()
    print user.name
    for image in user.images:
        print image.filename,
    print ''

def q_where_exists():
    from sqlalchemy.sql import exists
    stmt = exists().where(Image.owner_id==User.id)
    for name, in session.query(User.name).filter(stmt):
        print name
    stmt = exists().where(User.name=='not exists')
    for name, in session.query(User.name).filter(stmt):
        print name
    else:
        print 'not exists'

def q_any():
    # any()で自動でexistsの判定をしてくれる。
    for row in session.query(User).filter(User.images.any()):
        print row.name

def q_any_with_filter():
    for row in session.query(User).filter(User.images.any(Image.filename.like('%5%'))):
        print row.name

if __name__ == '__main__':
    locals_dict = dict(locals())
    sample_func_list = [locals_dict[k] for k in sorted(locals_dict.keys()) if k.startswith('q_')]
    for func in sample_func_list:
        header(func.__name__)
        func()
        footer()


