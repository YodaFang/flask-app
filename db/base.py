from peewee import *
from playhouse.pool import PooledSqliteExtDatabase
import os

# db_file = os.getenv("DB_SQLLITE_FILE")
db = PooledSqliteExtDatabase("db.data", max_connections=10)

class Base(Model):
    class Meta:
        database = db

class User(Base):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

class Product(Base):
    name_cn = CharField()
    name_ro = CharField()
    bbd = DateField()

db.connect()
db.create_tables([User, Product])