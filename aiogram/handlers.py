import random

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import telegram_bot.aiogram_bot.app.keyboards as kb
import telegram_bot.aiogram_bot.app.weather as w
import telegram_bot.aiogram_bot.app.currency as cur
import telegram_bot.aiogram_bot.app.quote_of_the_day as quote

#создание экземпляра класса Router
router = Router()

#обработка команды /start
@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer('Привет!', reply_markup=kb.main)

#обработка кнопок основного меню
@router.message(F.text == 'Погода')
async def cmd_weather(message:Message):
    await message.answer('Погода', reply_markup=kb.weather)

@router.message(F.text == 'Курсы валют')
async def cmd_weather(message:Message):
    await message.answer('Курсы валют', reply_markup=kb.currency)

@router.message(F.text == 'В главное меню')
async def cmd_menu(message:Message):
    await message.answer('В главное меню', reply_markup=kb.main)


#обработка кнопки подменю 'Цитата дня' с выводом рандомной цитаты
@router.message(F.text == 'Цитата дня')
async def cmd_quote(message:Message):
    await message.answer(random.choice(quote.motivation))


#обработка кнопок подменю 'Погода' с выводом температуры в выбранном городе
#если пользователь нажал кнопку 'Другой город' - обработка идет через регистрацию
#состояний пользователя, чтобы словить его ответ и вывести нужное значение

@router.message(F.text == 'Ростов-на-Дону')
async def cmd_weather(message:Message):
    weather = w.get_weather('Ростов-на-Дону')
    await message.answer(weather)

@router.message(F.text == 'Москва')
async def cmd_weather(message:Message):
    weather = w.get_weather('Москва')
    await message.answer(weather)

class City(StatesGroup):
    city = State()

@router.message(F.text == 'Другой город')
async def cmd_weather(message:Message, state:FSMContext):
    await state.set_state(City.city)
    await message.answer(
        'Введите полное название города на <b>русском</b> языке:',
        parse_mode='html')

@router.message(City.city)
async def cmd_temp(message:Message, state:FSMContext):
    await state.update_data(city=message.text)
    city = await state.get_data()
    weather = w.get_weather(city['city'])
    await message.answer(weather)
    await state.clear()


#обработка кнопок подменю 'Курсы валют' с выводом соответсвующего значения
#если пользователь нажал кнопку 'Другая валюта' - обработка идет через регистрацию
#состояний пользователя, чтобы словить его ответ и вывести нужное значение

@router.message(F.text == 'Курс Доллара')
async def cmd_currency(message:Message):
    dollar = cur.currency_dollar_evro('usd')
    await message.answer(dollar)

@router.message(F.text == 'Курс Евро')
async def cmd_currency(message:Message):
    dollar = cur.currency_dollar_evro('eur')
    await message.answer(dollar)

class Currency(StatesGroup):
    currency = State()

@router.message(F.text == 'Другая валюта')
async def cmd_currency(message:Message, state:FSMContext):
    await state.set_state(Currency.currency)
    await message.answer('Введите название валюты на <b>английском</b> языке:',
        parse_mode='html')

@router.message(Currency.currency)
async def cmd_get_currency(message:Message, state:FSMContext):
    await state.update_data(currency=message.text)
    currency = await state.get_data()
    name_currency = cur.other_currency(currency['currency'])
    await message.answer(name_currency)
    await state.clear()



