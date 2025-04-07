from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


# Uzbekcha asosiy tugmalar
uz_file_convert = KeyboardButton("Faylni aylantirish 🔄")

uz_main_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(uz_file_convert)


# englizcha asosiy tugmalar

en_file_convert = KeyboardButton("File Convert 🔄")

en_main_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(en_file_convert)

# ruscha asosiy tugmalar

ru_file_convert = KeyboardButton("Конвертировать файл 🔄")


ru_main_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(ru_file_convert)










