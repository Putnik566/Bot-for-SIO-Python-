import asyncio

from headers import router
from create_bot import TOKEN_BOT, dp
from handlers.start import start_router



async def main():
    dp.include_router(router=router)
    dp.include_router(router=start_router)
    await dp.start_polling(TOKEN_BOT)# берём токен бота из файла config.py

if __name__ == "__main__" : #запуск модуля
    asyncio.run(main())