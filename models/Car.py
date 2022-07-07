from peewee import *
from .User import User

from extensions.database import BaseModel


class Car(BaseModel):
    name = CharField()
    model = CharField()
    user = ForeignKeyField(User, related_name='car_details')
