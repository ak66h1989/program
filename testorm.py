import os
path = 'C:/Users/ak66h_000/Documents/db/'
os.chdir(path)

import sqlalchemy
sqlalchemy.__version__
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
User.__table__
Base.metadata.create_all(engine)

e = create_engine('sqlite:///mysum.sqlite3') # ///relative path
connection = engine.connect()
connection = e.connect()

result = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
result = connection.execute("SELECT * FROM sqlite_master")

result = connection.execute("select * from forweb")
for row in result:
    # print(row)
    print("username:", row['漲跌(+/-)'])