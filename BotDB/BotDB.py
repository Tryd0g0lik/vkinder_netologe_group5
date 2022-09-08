import json
import sys

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from config import DSN
from BotDB.model import create_tables, Users, ElectedUsers, Filters, Lists, SearchValues
import os.path

class BotDB:
    def __init__(self):
        engine = sqlalchemy.create_engine(DSN)
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)
        session = self.Session()

        lists = session.query(Lists).all()
        if len(lists) == 0:
            script_dir = os.path.dirname(sys.argv[0])+'/BotDB'
            with open(os.path.join(script_dir, 'data.json'), 'rt') as f:
                data = json.load(f)
            for item in data:
                model = {
                    'list': Lists,
                    'filter': Filters
                }.get(item['model'])
                session.add(model(id=item.get('pk'), **item.get('fields')))
            session.commit()

        session.close()
