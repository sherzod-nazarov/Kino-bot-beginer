from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.config import kanal_id, kanal_linklar
from aiogram.types import InlineKeyboardButton

def KanallarButtons(id, bot):
    buttons = InlineKeyboardBuilder()
    for i in range(len(kanal_id)):
        buttons.add(InlineKeyboardButton(text="kanalga obuna bo'ling", url=kanal_linklar[i]))
    buttons.add(InlineKeyboardButton(text="Tekshirish", callback_data='tek'))
    buttons.adjust(1)
    return buttons.as_markup()
