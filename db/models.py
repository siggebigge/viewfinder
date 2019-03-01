from db.db_connection import BaseModel
from peewee import *


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    password = CharField()
