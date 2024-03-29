import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode

from service import Service

f = open(".api_telegram", "r")
API_TOKEN = f.read()


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

records = Service().get_tips("appCixhrwO39DH3D5", "tbly63ArWXouoPqVR")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)
@dp.message_handler(commands=['tip'])
async def new_tip(message: types.Message):
    tip = records.get_random_text()
    await message.answer(tip.__repr__(), parse_mode=tip.parse_mode)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
