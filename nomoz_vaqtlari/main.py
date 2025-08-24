

from app.token import token
from app.handler import router
import asyncio
import logging
from aiogram import Bot, Dispatcher, Router

async def main():
    bot=Bot(token, )
    dp=Dispatcher()
    # Register router
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig (level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('EXIT')









