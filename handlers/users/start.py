from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.file_convert_inline import inline_languages
from loader import dp
import mysql.connector
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from loader import bot



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"👋 {message.from_user.full_name} (Uz🇺🇿)Foydalanishdan oldin tilni tanlang.\n(En🇬🇧)Choose a language before use.\n(Ru🇷🇺)Перед использованием выберите язык. !!!", reply_markup=inline_languages)
    user_id = message.from_user.id
    username = message.from_user.username or "Noma'lum"

    user_added = await add_user_to_db(user_id, username)

    if user_added:
        await message.reply("Siz muvaffaqiyatli qo'shildingiz!")
    else:
        await message.reply("Siz allaqachon bazada mavjud ekansiz!")

@dp.message_handler(commands=['statistic'])
async def show_statistic(message: types.Message):
    user_count = await get_user_count()
    await message.reply(f"Hozirda {user_count} foydalanuvchi mavjud.")




# Bot va Dispatcher yaratish
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# MySQL ulanishi
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='magicfile'
)
cursor = db.cursor()

# Foydalanuvchini qo'shish funktsiyasi
async def add_user_to_db(user_id, username):
    cursor.execute("SELECT COUNT(*) FROM users WHERE user_id = %s", (user_id,))
    count = cursor.fetchone()[0]

    if count == 0:  # Agar foydalanuvchi mavjud bo'lmasa
        cursor.execute("INSERT INTO users (user_id, username) VALUES (%s, %s)", (user_id, username))
        db.commit()
        return True  # Foydalanuvchi qo'shildi
    return False  # Foydalanuvchi mavjud

# Foydalanuvchilar sonini olish funktsiyasi
async def get_user_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]

