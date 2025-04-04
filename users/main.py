from aiogram.types import Message, CallbackQuery
from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from database.main import ReadFilm, BarchaKinolar
from filter.filter import CheksupChanel
from buttons.main import KanallarButtons

user_router = Router()



@user_router.message(CommandStart(), CheksupChanel())
async def StartBot(message: Message):
    id = message.from_user.id
    await message.answer("Assalomu alaykum bro", reply_markup=KanallarButtons(id))
    

@user_router.message(F.text)
async def BotMessage(message: Message, bot: Bot):
    id = message.text
    user_id = message.from_user.id
    if id.isdigit():
        if id in BarchaKinolar():
            kino = ReadFilm(id=id)
            await message.answer_video(video=kino[3], caption=f"Nomi: {kino[1]}\nXaqida:\n{kino[2]}")
        else:
            await message.answer("bunday kino mavjud emas")
    else:
        await message.answer("raqam yuboring iltimos")


@user_router.callback_query(F.data)
async def Tekshirish(call: CallbackQuery, bot: Bot):
    id = call.from_user.id    
    await call.message.answer("Kanalga obuna bo'ling", reply_markup=KanallarButtons(id))