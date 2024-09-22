from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
    
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Узнать координаты",request_location=True)
        ]
    ],
    resize_keyboard=True
)

