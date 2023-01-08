from aiogram import Bot, types, Dispatcher
from data import config

from aiogram.contrib.fsm_storage.redis import RedisStorage2


bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = RedisStorage2(db=5)

dp = Dispatcher(bot, storage=storage)