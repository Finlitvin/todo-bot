from database import db
from .userModel import User
from .taskModel import Task


def create_all_models():
    with db.db:
        db.db.create_tables([User, Task])
    print('DB CREATE')
