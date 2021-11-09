from database import db
from models import taskModel


def create_task(user_id, body):
    """ Создаём задание в БД """
    with db.db:
        taskModel.Task.create(user_id=user_id, body=body)


def delete_task(id):
    """ Удаляем задачу из БД """
    with db.db:
        taskModel.Task.delete_by_id(id)


def get_all_tasks(user_id):
    """ Получаем все задания пользователя """

    with db.db:
        tasks = taskModel.Task.select().where(taskModel.Task.user_id == user_id).dicts()
    return tasks


def get_task(user_id, id):
    """ Получаем все задачи определённого пользователя """

    with db.db:
        task = taskModel.Task.get_or_none(user_id=user_id, id=id)
    return task
