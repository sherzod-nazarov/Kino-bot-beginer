from aiogram import Bot, Dispatcher
from data.config import tokken, admin
import asyncio
from users.main import user_router
from admin.main import admin_router

bot = Bot(token=tokken)
dp = Dispatcher()

dp.include_router(admin_router)
dp.include_router(user_router)


async def main():
    for id in admin:
        await bot.send_message(chat_id=id, text="Bot ishga tushdi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try: 
        asyncio.run(main())
    except:
        print("Bot faolyatini tugatdi")