from data.config import kanal_id
from aiogram.filters import Filter
from aiogram.types import Message
from aiogram import Bot

class  CheksupChanel(Filter):
    async def __call__(self, message: Message, bot: Bot):
        # for i in range(len(kanal_id)):
        user_status = await bot.get_chat_member(kanal_id[0], message.from_user.id)
        if user_status.status in ['creator', 'administrator', "member"]:
             return False
        return True 
