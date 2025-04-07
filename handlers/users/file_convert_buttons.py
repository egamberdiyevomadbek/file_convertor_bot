from aiogram import types
from loader import dp
from keyboards.inline.file_convert_inline import inline_uz_buttons, inline_en_buttons, inline_ru_buttons

@dp.message_handler(text="Faylni aylantirish 🔄")
async def file_convert_uz(message: types.Message):
    await message.reply(
        "Faylni aylantirish 🔄", reply_markup=inline_uz_buttons
    )

@dp.message_handler(text="File Convert 🔄")
async def file_convert_en(message: types.Message):
    await message.reply(
        "Faylni aylantirish 🔄", reply_markup=inline_en_buttons
    )

@dp.message_handler(text="Конвертировать файл 🔄")
async def file_convert_ru(message: types.Message):
    await message.reply(
        "Faylni aylantirish 🔄", reply_markup=inline_ru_buttons
    )