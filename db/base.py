from peewee import *
from playhouse.pool import PooledSqliteDatabase
import os
import datetime

# db_file = os.getenv("DB_SQLLITE_FILE")
db_file = "db.data"
db = PooledSqliteDatabase(db_file, max_connections=10)

class Base(Model):
    class Meta:
        database = db

class User(Base):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

class Product(Base):
    name_cn = CharField(500)
    name_ro = CharField(500)
    bbd = DateField()
    updated_at = DateTimeField(default=datetime.datetime.now)  # 自动更新的字段

if not os.path.exists(db_file):
    db.connect()
    db.create_tables([User, Product])