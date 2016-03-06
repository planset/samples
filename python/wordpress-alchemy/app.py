# -*- coding: utf-8 -*-

import sqlalchemy as sa
import wpalchemy.classes as wp
from sqlalchemy.sql.expression import desc, asc

engine = sa.create_engine('mysql://webuser:webuser@localhost/heteml?charset=utf8')
session = sa.orm.sessionmaker(engine)()

posts = session.query(wp.Post).filter(wp.Post.post_status == 'publish').order_by(desc(wp.Post.post_date)).limit(10)
for post in posts:
    print post.post_title.encode("utf-8")


