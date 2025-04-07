from aiogram import Bot, Dispatcher, F, types
from data.config import tokken, admin
import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import and_f
from users.main import user_router
from admin.main import admin_router
from Group.main import group_router

bot = Bot(token=tokken,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


dp.include_router(group_router)
dp.include_router(admin_router)
dp.include_router(user_router)




# @dp.message(F.text=="salom", F.chat.type == "supergroup")
# async def get_guruh(message: types.Message):
#     await message.answer(f"{message.chat.title}\n{message.chat.type}\n{message.chat.id}")


# @dp.message(and_f(F.chat.type == 'supergroup', F.new_chat_members))
# async def get_new_chat(message: types.Message):
#     for new_chat in message.new_chat_members:
#         await message.answer(f"Assalomu alaykum guruhga xush kelibsiz {new_chat.full_name}")
#         await message.delete()



# @dp.message(and_f(F.chat.type == 'supergroup', F.left_chat_member ))
# async def get_left_chat(message: types.Message):
#     await message.answer(f"Xayr bro {message.left_chat_member.full_name}")



# @dp.message(and_f(F.chat.type == 'supergroup', F.new_chat_members))
# async def get_new_chat(message: types.Message):
#     for new_chat in message.new_chat_members:
#         await message.answer(f"Assalomu alaykum guruhga xush kelibsiz {new_chat.full_name}")
#         await message.delete()



# @dp.message(and_f(F.chat.type == 'supergroup', F.left_chat_member ))
# async def get_left_chat(message: types.Message):
#     await message.answer(f"Xayr bro {message.left_chat_member.full_name}")




# @dp.message(F.chat.type == 'supergroup', and_f(F.text == "yozma", F.reply_to_message))
# async def get_banned_chat(message: types.Message): 
#    user_id = message.reply_to_message.from_user.id
#    permsions = types.ChatPermissions(can_send_messages=False)
#    await message.chat.restrict(user_id, permsions)
#    await message.answer(f"Siz notog'ri so'zdan foydlaandizngiz\n🚫 {message.reply_to_message.from_user.full_name}")



# @dp.message(F.chat.type == 'supergroup',and_f(F.text == "yoz", F.reply_to_message))
# async def get_not_ban_chat(message: types.Message):
#    user_id = message.reply_to_message.from_user.id
#    permsions = types.ChatPermissions(can_send_messages=True)
#    await message.chat.restrict(user_id, permsions)
#    await message.answer(f"Siz endi yoza olasiz\n🆗 {message.reply_to_message.from_user.full_name}")

# @dp.message(F.chat.type == "supergroup",and_f(F.text == "ban", F.reply_to_message))
# async def get_bann_chat(message: types.Message):
#    user_id = message.reply_to_message.from_user.id
#    await message.chat.ban_sender_chat(user_id)
#    await message.answer(f"Siz guruhdan haydaldingiz\n ❌ {message.reply_to_message.from_user.full_name}")



# @dp.message(F.chat.type == "supergroup",and_f(F.text == "unban", F.reply_to_message))
# async def get_unbann_chat(message: types.Message):
#    user_id = message.reply_to_message.from_user.id
#    await message.chat.unban_sender_chat(user_id)
#    await message.answer(f"Siz endi guruhga qo'shila olasiz\n 🆗 {message.reply_to_message.from_user.full_name}")


async def main():
    for id in admin:
        await bot.send_message(chat_id=id, text="Bot ishga tushdi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try: 
        asyncio.run(main())
    except:
        print("Bot faolyatini tugatdi")
