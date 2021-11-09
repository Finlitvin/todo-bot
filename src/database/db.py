from peewee import *
import os
from dotenv import load_dotenv


load_dotenv(override=True)

db = SqliteDatabase(os.environ.get('DB_NAME'))
