from aiogram import Dispatcher
from .middleware_and_antiflood import ThrottlingMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())