import emoji


start_messages = """
{zap_emoji} Добро пожаловать {zap_emoji}
Список команд - /help
""".format(zap_emoji=emoji.emojize(':zap:', use_aliases=True))


help_messages = """
{zap_emoji} Справка {zap_emoji}
Установить напоминание - /new
Посмотреть список активных напоминайний - /list
Удалить напоминание - /done
""".format(zap_emoji=emoji.emojize(':zap:', use_aliases=True))
