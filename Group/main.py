from aiogram.types import Message, ChatPermissions
from aiogram import Router, F
from aiogram.filters import and_f
from aiogram.filters import CommandStart


group_router = Router()

@group_router.message(CommandStart(), F.chat.type == "supergroup")
async def StartGroup(message: Message):
    await message.answer("Guruhdan Salom sizga")

@group_router.message(F.chat.type == "supergroup",F.new_chat_members)
async def get_guruh(message: Message):
    for i in message.new_chat_members:
        await message.answer(f"Assalomu alaykum Guruhga xush kelibsiz {i.first_name}")

@group_router.message(and_f(F.chat.type == 'supergroup', F.left_chat_member))
async def get_left_chat(message: Message):
    await message.answer(f"Xayr bro {message.left_chat_member.full_name}")




@group_router.message(F.chat.type == 'supergroup', and_f(F.text == "yozma", F.reply_to_message))
async def get_banned_chat(message: Message): 
   user_id = message.reply_to_message.from_user.id
   permsions = ChatPermissions(can_send_messages=False)
   await message.chat.restrict(user_id, permsions)
   await message.answer(f"Siz notog'ri so'zdan foydlaandizngiz\n🚫 {message.reply_to_message.from_user.full_name}")



@group_router.message(F.chat.type == 'supergroup',and_f(F.text == "yoz", F.reply_to_message))
async def get_not_ban_chat(message: Message):
   user_id = message.reply_to_message.from_user.id
   permsions = ChatPermissions(can_send_messages=True)
   await message.chat.restrict(user_id, permsions)
   await message.answer(f"Siz endi yoza olasiz\n🆗 {message.reply_to_message.from_user.full_name}")

