import aiogram
import asyncio
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram import types
from aiogram import F
from aiogram.types import FSInputFile
from crud_functions import get_all_products


api = '7706256202:AAEVx4cyEY9PFDv-EB9yzLuPEdkbA62Y-BI'
bot = aiogram.Bot(token=api)
dp = aiogram.Dispatcher(storage=MemoryStorage())


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Рассчитать"),
            types.KeyboardButton(text="Информация"),

        ],
        [
            types.KeyboardButton(text="Купить")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=keyboard)


@dp.message(F.text.lower() == "купить")
async def get_buying_list(message: aiogram.types.Message):
    records = get_all_products()
    for product in records:
        title, description, price = product
        p_1 = FSInputFile(f"{price}.jpg")
        await message.answer_photo(p_1, f"Название: {title} | Описание: {description} | Цена: {price}")
    kb = [
        [
            types.InlineKeyboardButton(text="Продукт 1", callback_data='product_buying'),
            types.InlineKeyboardButton(text="Продукт 2", callback_data='product_buying'),
            types.InlineKeyboardButton(text="Продукт 3", callback_data='product_buying'),
            types.InlineKeyboardButton(text="Продукт 4", callback_data='product_buying'),
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=kb,
        resize_keyboard=True)
    await message.answer("Выберите продукт для покупки:", reply_markup=keyboard)


@dp.callback_query(F.data == 'product_buying')
async def get_formulas(callback: types.CallbackQuery):
    await callback.message.answer("Продукт успешно приобретён!")
    await callback.answer()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(F.text.lower() == "рассчитать")
async def main_menu(message: aiogram.types.Message):
    kb =  [
        [
            types.InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories'),
            types.InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=kb,
        resize_keyboard=True)
    await message.answer("Выберите опцию", reply_markup=keyboard)


@dp.callback_query(F.data == 'formulas')
async def get_formulas(callback: types.CallbackQuery):
    await callback.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await callback.answer()


@dp.callback_query(F.data == "calories")
async def set_age(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserState.age)
    await callback.message.answer("Введите свой возраст")
    await callback.answer()


@dp.message(UserState.age)
async def set_growth(message: aiogram.types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(UserState.growth)
    await message.answer("Введите свой рост в сантиметрах")


@dp.message(UserState.growth)
async def set_weight(message: aiogram.types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await state.set_state(UserState.weight)
    await message.answer("Введите свой вес в киллограмах")


@dp.message(UserState.weight)
async def send_calories(message: aiogram.types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    weight = float(data.get('weight'))
    growth = float(data.get('growth'))
    age = float(data.get('age'))
    cal = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма каллорий: {cal}')
    await state.clear()


@dp.message()
async def cmd_test1(message: aiogram.types.Message):
    await message.answer("Введите команду /start, чтобы начать общение..")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
