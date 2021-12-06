import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "1990527566:AAEOHVU71WKFHttlWCWNo9uisa_A8cchrUQ"
CHAT_ID = "728491010"

# Задаем уровень логов
logging.basicConfig(level=logging.INFO)

# Инициализируем бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# эхо
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# Запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)