import logging
import requests

from FastApiRequest import send_request
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)
bot = Bot(token='token')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    data_to_pass = message.get_args()
    print (data_to_pass)
    user_id = send_request(data_to_pass)
    print(user_id)
    if user_id[1] == message.from_user.id:
        await message.reply("Ошибка - аккаунт уже был привязан", parse_mode=ParseMode.MARKDOWN)
    elif user_id == 'error' or user_id[0] == None:
        await message.reply("Поризошла ошибка", parse_mode=ParseMode.MARKDOWN)
    else:
        await message.reply("Аккаунт успешно привязан", parse_mode=ParseMode.MARKDOWN)
        user_id = message.from_user.id

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)