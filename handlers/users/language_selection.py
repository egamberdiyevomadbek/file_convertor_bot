from aiogram import types
from loader import dp
from keyboards.default.main_buttons import uz_main_buttons, ru_main_buttons, en_main_buttons

@dp.callback_query_handler()
async def python_basic(call: types.CallbackQuery):
    text = call.data
    if text == "uzbek_tili":
        await call.message.answer("Assalomu alaykum MagicFile Botga xush kelibsiz !", reply_markup=uz_main_buttons)
    elif text == 'english':
        await call.message.answer("Hello. Welcome to MagicFile Bot !", reply_markup=en_main_buttons)
    elif text == 'rus_tili':
        await call.message.answer("Привет. Добро пожаловать в бот MagicFile !", reply_markup=ru_main_buttons)










