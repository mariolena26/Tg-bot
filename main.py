import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os

API_TOKEN = "7535665268:AAFTBdOjciCRWNiDfLP0LSXDVon18JoJs38"
CHANNEL_USERNAME = "@chilldrawing"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

user_data = {}

age_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
age_keyboard.add(KeyboardButton("Так"), KeyboardButton("Ні"))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    chat_member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
    if chat_member.status not in ['member', 'creator', 'administrator']:
        await message.answer("Щоб продовжити, підпишіться на канал: https://t.me/chilldrawing")
        return
    await message.answer("На каналі контент 18+. Підтвердіть свій вік для вашої ж відповідальності:", reply_markup=age_keyboard)

@dp.message_handler(commands=['age'])
async def change_age(message: types.Message):
    await message.answer("Підтвердіть свій вік ще раз:", reply_markup=age_keyboard)

@dp.message_handler(lambda message: message.text in ["Так", "Ні"])
async def handle_age(message: types.Message):
    user_id = message.from_user.id
    if message.text == "Так":
        await message.answer("Ласкаво просимо! Ось посилання на канал: https://t.me/chilldrawing")
    else:
        await message.answer("Доступ заборонено. Контент лише для повнолітніх.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)