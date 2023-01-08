from aiogram import types
from loader import dp
from aiogram.types import ChatType
from utils.misc.throttling import rate_limit

@rate_limit(5, 'apology_ch')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='Бот извинись')
async def command_apology(message: types.Message):
    await message.answer("Прости")