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

class Template(Base):
    name = CharField(255)
    desc = CharField(500, null=True)
    width = CharField(100, null=True)
    height = CharField(100, null=True)
    font_size = CharField(100, null=True)
    updated_at = DateTimeField(default=datetime.datetime.now)  # 自动更新的字段


class Org(Base):
    code = CharField(255, unique=True)
    name1 = CharField(255, unique=True)
    name2 = CharField(255, null=True)
    name3 = CharField(255, null=True)
    email = CharField(255, null=True)
    tel = CharField(255, null=True)
    addr = CharField(500, null=True)
    website = CharField(500, null=True)
    updated_at = DateTimeField(default=datetime.datetime.now)  # 自动更新的字段

class Product(Base):
    org = ForeignKeyField(Org, backref='products')
    template = ForeignKeyField(Template)
    name_cn = CharField(500)
    name_ro = CharField(500)
    bbd = DateField()
    updated_at = DateTimeField(default=datetime.datetime.now)  # 自动更新的字段

if not os.path.exists(db_file):
    db.connect()
    db.create_tables([User, Org, Product])