import types
from aiogram import Bot, Dispatcher, types
from aiogram.filters import  CommandStart
from aiogram.types import Message
import asyncio
from kb import main_kb


bot = Bot("bot-key") #-your key
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Нажми на меня что бы узнать свое местоположение",reply_markup=main_kb)



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
