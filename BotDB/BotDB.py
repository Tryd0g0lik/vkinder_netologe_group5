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

        lists = session.query(Lists).count()
        filt = session.query(Filters).count()

        if lists == 0 or filt == 0:
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

    def insert_user(self, user_id):
        session = self.Session()
        count_user = session.query(Users).filter(Users.id == user_id).count()
        if count_user == 0:
            session.add(Users(id=user_id, token=user_id))
            # id = sq.Column(sq.Integer, primary_key=True)
            # id_user = sq.Column(sq.Integer, sq.ForeignKey("user.id"), nullable=False)
            # id_filter = sq.Column(sq.Integer, sq.ForeignKey("filter.id"), nullable=False)
            # values = sq.Column(sq.Integer)
            filters = session.query(Filters).all()

            for item in filters:
                print(item.id)
            # session.add(SearchValues(id_user=user_id, id_filter))
            print("Insert User")
        session.commit()
        session.close()
        return True
