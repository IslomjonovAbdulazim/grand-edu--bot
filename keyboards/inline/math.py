from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

math_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👋Kursga yozilish", callback_data="27.secret.go.math.course"),
        ],
    ],
    resize_keyboard=True,
)
