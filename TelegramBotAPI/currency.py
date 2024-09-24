import datetime
from pycbrf import ExchangeRates


def currency_value(currency: str) -> str:
    """
        Возвращает значение валюты, выбранной пользователем, на сегодняшний день.
        Обрабатыввет ошибку в случае неверного написания названия валюты.
    """
    try:
        currency = currency.upper()
        rates = ExchangeRates(datetime.datetime.now())
        message = f'1 {currency} равен {round(rates[currency].rate, 2)} RUB.'
    except Exception:
        message = 'Неверный формат. Введите значение валюты на английском языке: '

    return message