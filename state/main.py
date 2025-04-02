from aiogram.fsm.state import State, StatesGroup


class Kinolar(StatesGroup):
    name = State()
    des = State()
    url = State()

