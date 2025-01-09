from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = ''
bot = Bot(token=api)
dispatcherBot = Dispatcher(bot, storage=MemoryStorage())





@dispatcherBot.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dispatcherBot.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dispatcherBot, skip_updates=True)