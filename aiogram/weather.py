import requests
import json
from telegram_bot.aiogram_bot.config import API

def get_weather(city):
    """возвращает значение температуры в городе, выбранном пользователем."""

    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city.lower().strip()}&appid={API}&units=metric')

    #если пользователь ввел город правильно - идет обработка запроса,
    #в противном случае - возвращается сообщение о небходимости ввести город правильно
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = round(data['main']['temp'])
        message = f"Погода в городе {city.title()} сейчас: {temp} °C"
    else:
        message = 'Такого города не существует.\nВведите правильное название города.'

    return message
