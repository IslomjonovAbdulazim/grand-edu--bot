from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📍Lokatsiyamiz", callback_data="27.secret.go", url='https://maps.app.goo.gl/XrhNf54iU7UiAdVy8'),
        ],
    ],
    resize_keyboard=True,
)
