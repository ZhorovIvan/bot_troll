from aiogram import types
from loader import dp

@dp.message_handler(text='/help')
async def command_start(message: types.Message):
    await message.answer('Данная версия бота присылает хорошие \n'
                        '(не такие херовые как у Тёмыча) анекдоты. \n'
                        'Иногда подкалывает! \n'
                        'В следующей версии будет: \n'
                        '   1)Анализ, кто главный пездобол за день \n'
                        '   2)Конвертация текста в аудио')