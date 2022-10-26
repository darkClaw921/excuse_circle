import random
from loguru import logger
from art import text2art
from dotenv import load_dotenv
from aiogram.types import InputFile
from pprint import pprint
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.types.message import ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

logger.add('log.log', level='DEBUG')

load_dotenv()
tgToken = os.environ.get('TG_TOKEN')

bot = Bot(token=str(tgToken)) 
dp = Dispatcher(bot,storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
sticers = ['CAACAgIAAxkBAAEGNhxjWbhNyUy03_23sHJw4x-PozFEPAACJygAAs5a0UqMKBlggLIYxyoE',
           'CAACAgIAAxkBAAEGNh5jWbhR5Y2slbCgQ92AKZYd9olJmgACwR4AAqh_0UreBOLLdiV3dioE',
           'CAACAgIAAxkBAAEGNiBjWbhSzT-GZWeOIBLKpBRyPl9tzwACDBwAAsgw0Eq8pOohczNGcSoE',
           'CAACAgIAAxkBAAEGNiRjWbzi5KERR5e0Uyf-bMorjcS1YAACayIAAuYYyEoEqeRJSKYgnCoE',
           'CAACAgIAAxkBAAEGNiZjWbzkliI-DhfnY2XxgwFPtV-IswACYSQAAm6KyUr-u66z2ClFIyoE',
           'CAACAgIAAxkBAAEGNihjWbzmfBE3Dr2-5TSW0QF2wIdpVAAC0SUAAjfDyEqKCb0Ms8X-JSoE',
           'CAACAgIAAxkBAAEGNipjWbzobtMJ2aC-aN4_9axChwjtxwAC9SMAAjs9yUo3oR8DLrhXbSoE',
           'CAACAgIAAxkBAAEGNixjWbzuqD4tq1BPKhqnAn7HMML0VgACGiIAAifr0EpbqCs85jZLgSoE',
           'CAACAgIAAxkBAAEGNi5jWbzwnBBSPrnOhjuE25dpkkVNRQACQScAAsG9yUr7L1wyjjfrNSoE',
           'CAACAgIAAxkBAAEGNjBjWbzxorOydsDaw4qS9UdVnxYRowACpyIAAhHLyErdaaibMHT0LSoE',
           'CAACAgIAAxkBAAEGNjJjWbzzyZi3cLKSbP5eju7K04gFIAACeiQAAqvD0Ur7EFPzyTuVmSoE',
           'CAACAgIAAxkBAAEGNjRjWb4lUnxws_n8lrD90UO7TXkn4gACXiYAAlR30EoBocbmnFcgZCoE']

markup_first = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Жги')
)

slova = ['помоги',
'помогите',
'памагите',
'спасите',
'помоги',
'помощь',
'помочь',
'выручи',
'выручай',
'выручите',
'выручку',
'выручка',
'жги']

#@dp.message_handler(content_types=ContentType.ANY)
@dp.message_handler(lambda msg: any(word in msg.text.lower() for word in slova))
@logger.catch
async def echo_message(msg: types.Message):
    state = dp.current_state(user=msg.from_user.id)
    
    message = msg.text.lower()
    user_id = msg.from_user.id
    #pprint(msg)

    #await msg.answer_sticker(random.choice(sticers), reply_markup=markup_first)
    await bot.send_sticker(msg.chat.id,random.choice(sticers), reply_markup=markup_first)
    #await bot.send_message(msg.from_user.id, 'лох')
    #await state.set_state('firstMsg')



if __name__ == '__main__':
    art = text2art('fortuna', 'rand')
    print(art)
    #main()
    executor.start_polling(dp)

