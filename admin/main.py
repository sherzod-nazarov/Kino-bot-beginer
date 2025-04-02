from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import CommandStart
from data.config import admin
from aiogram.fsm.context import FSMContext
from state.main import Kinolar
from database.main import AddFilm


admin_router = Router()



@admin_router.message(CommandStart(), F.from_user.id.in_(admin))
async def StartBot(message: Message, state: FSMContext):
    await message.answer("Assalomu alaykum Admin\nKino nomini kiriting?")
    await state.set_state(Kinolar.name)




@admin_router.message(F.text, Kinolar.name)
async def StartBot(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Kino haqida malumot yuboring? ")
    await state.set_state(Kinolar.des)



@admin_router.message(F.text, Kinolar.des)
async def StartBot(message: Message, state: FSMContext):
    des = message.text
    await state.update_data(des=des)
    await message.answer("Kinoni yuboring ")
    await state.set_state(Kinolar.url)


@admin_router.message(F.video, Kinolar.url)
async def StartBot(message: Message, state: FSMContext):
    url = message.video.file_id
    data = await state.get_data()
    name = data.get('name')
    des = data.get('des')
    AddFilm(name=name, description=des, url=url)
    await message.answer("Kino qo'shildi")
    await state.clear()
