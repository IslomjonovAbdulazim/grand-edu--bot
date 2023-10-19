from aiogram.dispatcher.filters.state import StatesGroup, State


class PhoneState(StatesGroup):
    math = State()
    chemistry = State()

