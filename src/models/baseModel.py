from peewee import *
from database.db import db


class BaseModel(Model):
    class Meta:
        database = db
