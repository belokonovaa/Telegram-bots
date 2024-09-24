import requests
import json
from config import API

def get_weather(city: str) -> str:
    """
    Возвращает значение температуры на данный момент в городе, выбранном пользователем.
    Обрабатывает ошибку в случае неверного написания названия города.
    """

    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city.lower().strip()}&appid={API}&units=metric')

    if res.status_code == 200:
        data = json.loads(res.text)
        temp = round(data['main']['temp'])
        message = f"Погода в городе {city.title()} сейчас: {temp} °C"
    else:
        message = 'Такого города не существует.\nВведите правильное название города.'

    return message

