from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

chemistry_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👋Kursga yozilish", callback_data="27.secret.go.chemistry.course"),
        ],
    ],
    resize_keyboard=True,
)
