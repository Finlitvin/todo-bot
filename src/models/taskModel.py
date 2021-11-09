from peewee import *
import datetime as dt

from .baseModel import BaseModel
from .userModel import User


class Task(BaseModel):
    user_id = ForeignKeyField(User, to_field='user_id')
    body = TextField(column_name='body')
    created_date = DateField(column_name='created_date', default=dt.date.today())

    class Meta:
        table_name = 'tasks'
