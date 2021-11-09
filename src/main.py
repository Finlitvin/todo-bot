from bot import bot
from bot import handlers


def main():
    bot.bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
