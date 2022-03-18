import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types, utils
from aiogram.types import ParseMode
from config import TOKEN, URL


logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands = 'list')
async def send_list(message: types.message):
    message_text = 'Строка поиска {}'.format('123')
    await message.answer(text=message_text)

@dp.message_handler(commands = 'search')
async def send_search(message: types.message):
    message_text = 'Слова поиска {}'.format('123')
    await message.answer(text=message_text)


@dp.message_handler()
async def echo(message: types.message):
    await message.answer(text=message.text)


async def scheduled(wait_for, parser):
    while True:
        await asyncio.sleep(wait_for)
        print('Работаю!')
        pass
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10, None))
    executor.start_polling(dp, skip_updates=True)

