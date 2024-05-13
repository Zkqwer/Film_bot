import asyncio
import logging

from aiogram import Bot, Dispatcher
import settings
import database.db as db


async def main():
    from bot.routers import router as main_router
    dp = Dispatcher()
    dp.include_router(main_router)

    await db.delete_tables()
    await db.create_tables()

    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
