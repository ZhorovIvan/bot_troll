from aiogram import types
from loader import dp
from aiogram.types import ChatType
from utils.misc.throttling import rate_limit
import random
from utils.get_joke_from_api import get_joke
from data import config 

@rate_limit(5, 'joke_ch')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='[Аа]некдот')
async def command_joke(message: types.Message):
    joke_type = '1' if random.randint(0, 1) == 1 else '11'
    joke = await get_joke(joke_type)
    await message.answer(joke)


@rate_limit(5, 'toast_ch')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='[Тт]ост')
async def command_toast(message: types.Message):
    toast_type = '6' if random.randint(0, 1) == 1 else '16'
    toast = await get_joke(toast_type)
    await message.answer(toast)


@rate_limit(5, 'nope_ch')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL],  regexp='[Нн]ет.*')
async def command_toast(message: types.Message):
    # Add filter on middleware
    if str(message["from"]["id"]) in config.ADMINS_ID:
        return
    await message.reply('Пидора ответ')


@rate_limit(5, 'fatality_ch')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='.*[шШ]люхи аргумент.*')
async def command_toast(message: types.Message):
    # Add filter on middleware
    if str(message["from"]["id"]) in config.ADMINS_ID:
        return
    await message.reply('Аргумент не нужен пидор обнаружен')
    # path for linux
    with open('data/images/fatality.mp4', 'rb') as video:
        await message.answer_video(video)


@rate_limit(5, 'mom_ch')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='.*([шШ]люха|[Пп]роститутка).*')
async def command_mom(message: types.Message):
    # Add filter on middleware
    if str(message["from"]["id"]) in config.ADMINS_ID:
        return
    await message.reply('Шлюха твоя мамка')


@rate_limit(5, 'big_mom_ch')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='.*([Жж]ирн(ая|ый|ое|ую)|[Тт]олст(ая|ый|ое|ую)).*')
async def command_big_mom(message: types.Message):
    # Add filter on middleware
    if str(message["from"]["id"]) in config.ADMINS_ID:
        return
    await message.reply('Твоя мама такая толстая, что в ресторанах написано: \n'
                        '«Вместительность 300 человек, или твоя мама».')