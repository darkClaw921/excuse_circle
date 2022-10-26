
from loguru import logger
from art import text2art
from dotenv import load_dotenv
from aiogram.types import InputFile
from pprint import pprint

from aiogram.types.message import ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

logger.add('log.log', level='INFO')

load_dotenv()
tgToken = os.environ.get('TG_TOKEN')

bot = Bot(token=str(tgToken)) 
dp = Dispatcher(bot,storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
sticers = []



@dp.message_handler(content_types=ContentType.ANY)
@logger.catch
async def echo_message(msg: types.Message):
    state = dp.current_state(user=msg.from_user.id)
    
    message = msg.text.lower()
    user_id = msg.from_user.id
    pprint(msg)
    await bot.send_message(msg.from_user.id, 'лох')
    #await state.set_state('firstMsg')



if __name__ == '__main__':
    art = text2art('fortuna', 'rand')
    print(art)
    #main()
    executor.start_polling(dp)

