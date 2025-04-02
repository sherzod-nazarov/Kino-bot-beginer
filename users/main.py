from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import CommandStart
from database.main import ReadFilm, BarchaKinolar

user_router = Router()



@user_router.message(CommandStart())
async def StartBot(message: Message):
    await message.answer("Assalomu alaykum bro")


@user_router.message(F.text)
async def BotMessage(message: Message):
    id = message.text
    if id.isdigit():
        if id in BarchaKinolar():
            kino = ReadFilm(id=id)
            await message.answer_video(video=kino[3], caption=f"Nomi: {kino[1]}\nXaqida:\n{kino[2]}")
        else:
            await message.answer("bunday kino mavjud emas")
    else:
        await message.answer("raqam yuboring iltimos")