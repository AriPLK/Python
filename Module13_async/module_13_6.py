from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


api = ''
bot = Bot(token=api)
dispatcherBot = Dispatcher(bot, storage=MemoryStorage())
keyboard = InlineKeyboardMarkup(resize_keyboard=True)
caloriesButton = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')
infoButton = InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas')
keyboard.add(caloriesButton)
keyboard.add(infoButton)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dispatcherBot.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup = keyboard)


@dispatcherBot.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')



@dispatcherBot.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью!')



@dispatcherBot.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
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