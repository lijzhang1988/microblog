import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
engine = sa.create_engine("sqlite:////root/PycharmProjects/microblog/app/microblog.db")
DBSession = sessionmaker(engine)
session = DBSession()
