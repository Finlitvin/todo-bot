from database import db
from models import userModel


def create_user(user_id, username):
    """ Создаем пользователя в БД """

    with db.db:
        userModel.User.create(user_id=user_id, username=username)


def get_user(user_id):
    """ Получаем пользователя с БД, если пользователя нет, вернёт None """

    with db.db:
        user = userModel.User.get_or_none(user_id=user_id)
    return user
