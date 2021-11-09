import telebot
import os

from dotenv import load_dotenv


load_dotenv(override=True)

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

print('BOT: [CREATE]')
print(80 * '-')
print(bot.get_me())
print(80 * '-')
