from peewee import *

from extensions.database import BaseModel


class User(BaseModel):
    login = CharField(unique=True)
    password = CharField()
