# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config

# for mysql
# Engine Configuration — SQLAlchemy 0.7 Documentation <http://docs.sqlalchemy.org/en/rel_0_7/core/engines.html>`_
engine = create_engine(config.DATABASE,
                       encoding='utf-8',
                       isolation_level="READ UNCOMMITTED")

#
# parameter are READ COMMITTED, READ UNCOMMITTED, REPEATABLE READ, and SERIALIZABLE: 
# http://docs.sqlalchemy.org/en/rel_0_7/dialects/mysql.html#transaction-isolation-level 
#


#
# add sample data
#
Session = sessionmaker(bind=engine, autoflush=False)
Session.configure(bind=engine)
session = Session()

