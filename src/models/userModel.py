from peewee import *

from .baseModel import BaseModel


class User(BaseModel):
    user_id = IntegerField(column_name='user_id')
    username = FixedCharField(column_name='username', max_length=50)

    class Meta:
        table_name = 'users'
