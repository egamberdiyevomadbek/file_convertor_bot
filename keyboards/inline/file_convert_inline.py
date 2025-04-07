from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

uz = InlineKeyboardButton("Uz🇺🇿", callback_data="uzbek_tili")
en = InlineKeyboardButton("En🇬🇧", callback_data="english")
ru = InlineKeyboardButton("Ru🇷🇺", callback_data="rus_tili")

inline_languages = InlineKeyboardMarkup().row(uz,en, ru)





# uz_file_convert_inline_button

pdf_to_pptx = InlineKeyboardButton("PDF ni PPTX ga o'zgartirish 📄➡️📊", callback_data="uz_pdf_to_pptx")
jpg_to_png = InlineKeyboardButton("JPG ni PNG ga o'zgartirish 🖼️➡️📷", callback_data="uz_jpg_to_png")
json_to_csv = InlineKeyboardButton("JSON ni CSV ga o'zgartirish 📄➡️📈", callback_data="uz_json_csv")
zip = InlineKeyboardButton("Fayllarni ZIPga o'zgartirish 📦", callback_data="uz_zip")

inline_uz_buttons = InlineKeyboardMarkup().row(pdf_to_pptx).row(jpg_to_png).row(json_to_csv).row(zip)


# en_file_convert_button

en_pdf_to_pptx = InlineKeyboardButton("Convert PDF to PPTX 📄➡️📊", callback_data="en_pdf_to_pptx")
en_jpg_to_png = InlineKeyboardButton("Convert JPG to PNG 🖼️➡️📷", callback_data="en_jpg_to_png")
en_json_to_csv = InlineKeyboardButton("Convert JSON to CSV 📄➡️📈", callback_data="en_json_csv")
en_zip = InlineKeyboardButton("Convert files to ZIP 📦", callback_data="en_zip")

inline_en_buttons = InlineKeyboardMarkup().row(en_pdf_to_pptx).row(en_jpg_to_png).row(en_json_to_csv).row(en_zip)


# ru_file_convert_button

ru_pdf_to_pptx = InlineKeyboardButton("Конвертировать PDF в PPTX 📄➡️📊", callback_data="ru_pdf_to_pptx")
ru_jpg_to_png = InlineKeyboardButton("Конвертировать JPG в PNG 🖼️➡️📷", callback_data="ru_jpg_to_png")
ru_json_to_csv = InlineKeyboardButton("Конвертировать JSON в CSV 📄➡️📈", callback_data="ru_json_csv")
ru_zip = InlineKeyboardButton("Конвертировать файлы в ZIP 📦", callback_data="ru_zip")

inline_ru_buttons = InlineKeyboardMarkup().row(ru_pdf_to_pptx).row(ru_jpg_to_png).row(ru_json_to_csv).row(ru_zip)
