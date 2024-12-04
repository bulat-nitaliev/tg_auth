from decouple import config
from aiogram import Bot, Dispatcher
import asyncio, logging
from hendler.handlers import router
from datetime import datetime, date
import pytz   

mos = pytz.timezone('Europe/Moscow')
moscow_time = datetime.now(mos)

# rout = start if 0 < moscow_time.hour <  15 else start2

bot = Bot(token=config('API_TOKEN'))
dp = Dispatcher()
channel_id = config('CHANNEL_ID')



async def main():
    dp.include_router(router)
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')