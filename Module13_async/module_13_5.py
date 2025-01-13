from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


api = ''
bot = Bot(token=api)
dispatcherBot = Dispatcher(bot, storage=MemoryStorage())
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
caloriesButton = KeyboardButton(text = 'Рассчитать')
infoButton = KeyboardButton(text = 'Информация')
keyboard.add(caloriesButton)
keyboard.add(infoButton)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dispatcherBot.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью!', reply_markup = keyboard)


@dispatcherBot.message_handler(text = 'Информация')
async def bot_info(message):
    await  message.answer('Здесь ничего нет : )')


@dispatcherBot.message_handler(text = 'Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dispatcherBot.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dispatcherBot.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dispatcherBot.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    personCalories = (10 * int(data['weight'])) + (6 * int(data['growth'])) + (5 * int(data['age'])) + 5
    await message.answer(f'Ваша норма калорий {personCalories}')
    await state.finish()


@dispatcherBot.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dispatcherBot, skip_updates=True)