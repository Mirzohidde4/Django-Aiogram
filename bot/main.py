from aiogram import Bot,Dispatcher
import sys, logging
from aiogram.client.bot import DefaultBotProperties
from .handler.private import user_private_router
from config.settings import BOT_TOKEN


bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
ds = Dispatcher()
ds.include_router(user_private_router)


async def main():
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        await ds.start_polling(bot)
    except:
        pass
