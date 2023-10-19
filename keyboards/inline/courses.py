from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

courses_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕Matematika", callback_data="27.secret.matematika"),
        ],
        # [
        #     InlineKeyboardButton(text="Ingliz tili", callback_data="27.secret.ingliz"),
        # ],
        # [
        #     InlineKeyboardButton(text="Rus tili", callback_data="27.secret.rus"),
        # ],
        [
            InlineKeyboardButton(text="🧪Kimyo", callback_data="27.secret.kimyo"),
        ],
        # [
        #     InlineKeyboardButton(text="Bialogiya", callback_data="27.secret.bialogiya"),
        # ],
    ],
    resize_keyboard=True
)
