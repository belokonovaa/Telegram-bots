from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#создание кнопок основного меню
main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Цитата дня')],
        [KeyboardButton(text='Погода'), KeyboardButton(text='Курсы валют')]
        ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню:')

#создание кнопок подменю "Погода"
weather = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ростов-на-Дону'), KeyboardButton(text='Москва')],
        [KeyboardButton(text='Другой город'), KeyboardButton(text='В главное меню')]
        ],
    resize_keyboard=True,
    input_field_placeholder='Выберите город:')

#создание кнопок подменю "КУрсы валют"
currency = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Курс Доллара'), KeyboardButton(text='Курс Евро')],
        [KeyboardButton(text='Другая валюта'), KeyboardButton(text='В главное меню')]
        ],
    resize_keyboard=True,
    input_field_placeholder='Выберите валюту:')

