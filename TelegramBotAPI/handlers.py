import random
import telebot

import keyboards as kb
from quote_of_the_day import motivation
from weather import get_weather
from currency import currency_value


def command_start(bot: telebot.TeleBot) -> None:
    """ Обработка команды /start"""

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id,
                         f'Привет, {message.from_user.first_name}!'
                         f'\nЯ твой персональный бот-помощник.'
                         '\nРасскажу всю новую информацию и пожелаю удачи на день!',
                         reply_markup=kb.main)


def commands(bot: telebot.TeleBot) -> None:
    """
        Основная функция для обработки команд бота.
        Регистрирует обработчики сообщений для разных команд.
    """


    @bot.message_handler(content_types=['text'])
    def get_command(message: str) -> None:
        """
            Обработчик текстовых сообщений, который реагирует на команды пользователя.
        """

        response_mapping = {
            'Цитата дня': lambda:bot.send_message(message.chat.id, random.choice(motivation)),
            'Погода': lambda:bot.send_message(message.chat.id, 'Погода', reply_markup=kb.weather),
            'Курсы валют': lambda: bot.send_message(message.chat.id, 'Курсы валют', reply_markup=kb.currency),
            'В главное меню' : lambda: bot.send_message(message.chat.id, 'В главное меню', reply_markup=kb.main),
            'Ростов-на-Дону' : lambda : bot.send_message(message.chat.id, get_weather('Ростов-на-Дону')),
            'Москва': lambda : bot.send_message(message.chat.id,get_weather('Москва')),
            'Курс Доллара': lambda : bot.send_message(message.chat.id, currency_value('usd')),
            'Курс Евро': lambda : bot.send_message(message.chat.id, currency_value('eur'))
        }

        if message.text in response_mapping:
            response_mapping[message.text]()
        elif message.text == 'Другой город':
            ask_for_city(message)
        elif message.text == 'Другая валюта':
            ask_for_currency(message)


    def ask_for_city(message: str) -> None:
        """
            Запрашивает у пользователя название города для получения прогноза погоды.
        """
        bot.send_message(message.chat.id,
                             'Введите полное название города на <b>русском</b> языке:',
                             parse_mode='html')
        bot.register_next_step_handler(message, get_city)


    @ bot.message_handler(content_types=['text'])
    def get_city(message: str) -> None:
        """
            Обработчик для получения названия города от пользователя
            и отправки прогноза погоды.
        """
        city_name = message.text
        weather_city = get_weather(city_name)
        bot.send_message(message.chat.id, weather_city)


    def ask_for_currency(message: str) -> None:
        """
            Запрашивает у пользователя название валюты для получения курса.
        """
        bot.send_message(message.chat.id,
                             'Введите название валюты <b>на английском</b> языке:',
                             parse_mode='html')
        bot.register_next_step_handler(message, get_currency)


    @bot.message_handler(content_types=['text'])
    def get_currency(message: str) -> None:
        """
            Обработчик для получения валюты от пользователя и отправки курса.
        """

        currency_name = message.text
        currency = currency_value(currency_name)
        bot.send_message(message.chat.id, currency)