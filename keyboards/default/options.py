from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

courses_default = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📁Kurslar"),
            KeyboardButton(text="ℹ️Taklif & Shikoyatlar"),
        ],
        [
            KeyboardButton(text="📝Kursga yozilish"),
            KeyboardButton(text="📞Kontaktlar"),
        ]
    ],
    resize_keyboard=True
)