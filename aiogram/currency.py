from pycbrf import ExchangeRates
import datetime

def currency_dollar_evro(currency):
    """возвращает курс доллара или евро на сегодняшний день
        в отформатированном виде"""

    values = currency.upper()
    rates = ExchangeRates(datetime.datetime.now())
    message = f'1 {values} равен {round(rates[values].rate, 2)} RUB.'

    return message

def other_currency(currency):
    """возвращает курс валюты, введенной пользователем, на сегодняшний день
        в отформатированном виде. Если пользователь неправильно ввел название
        валюты - возвращается сообщение о неверном формате валюты"""

    try:
        currency = currency.upper()
        rates = ExchangeRates(datetime.datetime.now())
        message = f'1 {currency} равен {round(rates[currency].rate, 2)} RUB.'
    except Exception:
        message = 'Неверный формат. Введите корректное название валюты: '

    return message