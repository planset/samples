from sqlalchemy import create_engine

import config
import models


engine = create_engine(config.DATABASE,
                       encoding='utf-8')

models.Base.metadata.drop_all(engine)

# eof

