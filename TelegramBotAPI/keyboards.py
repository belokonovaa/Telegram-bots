from telebot import types

# основное меню бота
main = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                 input_field_placeholder='Выбери пункт меню:')
btn1 = types.KeyboardButton('Цитата дня')
main.row(btn1)
btn2 = types.KeyboardButton('Погода')
btn3 = types.KeyboardButton('Курсы валют')
main.row(btn2, btn3)

# подменю бота для выбора города для прогноза погоды
weather = types.ReplyKeyboardMarkup(row_width=2,
                                    resize_keyboard=True,
                                    input_field_placeholder='Выберите город:')
bt1 = types.KeyboardButton('Ростов-на-Дону')
bt2 = types.KeyboardButton('Москва')
bt3 = types.KeyboardButton('Другой город')
bt4 = types.KeyboardButton('В главное меню')
weather.add(bt1, bt2, bt3, bt4)


# подменю бота для выбора валюты для получения курса
currency = types.ReplyKeyboardMarkup(row_width=2,
                                     resize_keyboard=True,
                                     input_field_placeholder='Выберите валюту:')
b1 = types.KeyboardButton('Курс Доллара')
b2 = types.KeyboardButton('Курс Евро')
b3 = types.KeyboardButton('Другая валюта')
b4 = types.KeyboardButton('В главное меню')
currency.add(b1, b2, b3, b4)
