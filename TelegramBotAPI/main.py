import telebot

from config import TOKEN
import handlers


# Инициализация бота с токеном
bot = telebot.TeleBot(token=TOKEN)

# Регистрация обработчиков команд
handlers.command_start(bot)  # Обработка команды /start
handlers.commands(bot)  # Обработка остальных команд

# Запуск бота
bot.polling(none_stop=True)
