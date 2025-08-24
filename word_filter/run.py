
from datetime import timedelta
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ChatPermissions
import asyncio
import logging

bot=Bot(token=TOKEN)
dp=Dispatcher()

words=['yomon gaplar']
@dp.message(F.text)
async def word_check(message: Message):
    text=message.text.lower()
    if any(word in text for word in words):
        await message.reply('Siz yomon so\'z ishlatingiz!!!')

        until_date=message.date+timedelta(minutes=5)
        await message.bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.from_user.id,
            permissions=ChatPermissions(can_send_messages=False),
            until_date=until_date
        )




async def main():
    # Start polling only for the updates your handlers need
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig (level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')





