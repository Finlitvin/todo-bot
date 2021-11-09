from .bot import bot
from service import taskService
from service import userService
from .messages import *


@bot.message_handler(commands=['start'])
def start_msg(message):
    try:
        user_id = message.chat.id
        username = message.from_user.first_name

        result_msg = userService.create_user(user_id, username)
    except Exception as e:
        bot.send_message(message.chat.id, result_msg)


@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.send_message(message.chat.id, help_messages)


@bot.message_handler(commands=['list'])
def list_tasks(message):
    try:
        user_id = message.chat.id

        result_msg = taskService.get_all_tasks(user_id)

        bot.send_message(message.chat.id, result_msg)
    except Exception as e:
        bot.send_message(message.chat.id, 'Что-то пошло не так')


@bot.message_handler(commands=['new'])
def new_task(message):
    msg = bot.send_message(message.chat.id, 'Введите задачу')
    bot.register_next_step_handler(msg, process_task_step)


def process_task_step(message):
    try:
        user_id = message.chat.id
        body = message.text

        taskService.create_task(user_id, body)

        bot.send_message(message.chat.id, 'Задача добавлена')
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так')


@bot.message_handler(commands=['done'])
def done_task(message):
    msg = bot.send_message(message.chat.id, 'Введите номер задачи')
    bot.register_next_step_handler(msg, process_done_task_step)


def process_done_task_step(message):
    try:
        user_id = message.chat.id
        task_id = message.text

        result_msg = taskService.delete_task(user_id, task_id)

        bot.send_message(message.chat.id, result_msg)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так')