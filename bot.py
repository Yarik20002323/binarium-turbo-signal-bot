import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать в Binarium Turbo Signal!\n"
        "Команды:\n"
        "/signal — получить тестовый сигнал\n"
        "/profit — статистика прибыли\n"
        "/link — Binarium с бонусом"
    )

@dp.message_handler(commands=['signal'])
async def send_signal(message: types.Message):
    await message.answer(
        "📈 Сигнал: ВВЕРХ\n"
        "📊 EMA + RSI\n"
        "📉 RSI: 64 ↑\n"
        "⏱️ Срок: 1 минута\n"
        "🎯 Уверенность: 78%",
        parse_mode=ParseMode.MARKDOWN
    )

@dp.message_handler(commands=['link'])
async def send_link(message: types.Message):
    await message.answer("🎲 Binarium бонус: https://binarium.com/promo")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
