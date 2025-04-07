from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from data.config import admin
from aiogram.fsm.context import FSMContext
from state.main import Kinolar
from database.main import AddFilm
from database.admin_database import AddAdmins, ReadAdmins


admin_router = Router()
def Adminlar():
    malumot = []
    for i in ReadAdmins():
        malumot.append(i[1])
    return malumot    

@admin_router.message(Command("admins"))
async def AdminCommand(message: Message):
    id = message.from_user.id
    if id in Adminlar():
        await message.answer("Qo'shmoqchi bo'lgan admin id yuboring")


@admin_router.message(CommandStart())
async def StartBot(message: Message, state: FSMContext):
    id = message.from_user.id
    if id in Adminlar():
        await message.answer("Assalomu alaykum Admin\nKino nomini kiriting?")
        await state.set_state(Kinolar.name)




@admin_router.message(F.text)
async def AdminAdd(message: Message):
    id = message.text
    user_id = message.from_user.id
    if user_id in Adminlar():
        AddAdmins(id=int(id))
        await message.answer("Adminlar xatoriga qo'shildi")






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
