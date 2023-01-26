# Расписание
from datetime import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from ras import *

bot = Bot(TOKEN)
dp = Dispatcher(bot)


TODAY = date.today()
WEEKDAY = (TODAY.weekday()+1)
WEEKDAY1 = (TODAY.weekday()+2)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('Сегодня')).add(KeyboardButton('Завтра')).add(KeyboardButton('📆'))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Добро пожаловать в наш бот")
    await message.answer(text=MAKTAB,  reply_markup=kb)


@dp.message_handler(Text(equals='Сегодня'))
async def today(message: types.Message):
    if WEEKDAY == 1:
        await message.answer(pn)
    elif WEEKDAY == 2:
        await message.answer(vt)
    elif WEEKDAY == 3:
        await message.answer(sr)
    elif WEEKDAY == 4:
        await message.answer(cht)
    elif WEEKDAY == 5:
        await message.answer(pt)
    elif WEEKDAY == 6:
        await message.answer(sb)
    else:
        await message.answer(no)
    await message.delete()


@dp.message_handler(Text(equals='Завтра'))
async def tomarrov(message: types.Message):
    if WEEKDAY1 == 1:
        await message.answer(pn)
    elif WEEKDAY1 == 8:
        await message.answer(pn)
    elif WEEKDAY1 == 2:
        await message.answer(vt)
    elif WEEKDAY1 == 3:
        await message.answer(sr)
    elif WEEKDAY1 == 4:
        await message.answer(cht)
    elif WEEKDAY1 == 5:
        await message.answer(pt)
    elif WEEKDAY1 == 6:
        await message.answer(sb)
    else:
        await message.answer(no)
    await message.delete()


@dp.message_handler(Text(endswith='📆'))
async def cmd(message: types.Message):
    await message.answer(text='Расписание⬇️⬇️⬇️')
    await message.answer(pn)
    await message.answer(vt)
    await message.answer(sr)
    await message.answer(cht)
    await message.answer(pt)
    await message.answer(sb)
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
