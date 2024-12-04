from aiogram import types
from aiogram.filters import CommandStart
from aiogram import Router
from keyboard.keyboards import  inl_site
from fetchs.connect import register, login, islam
# import emoji

router = Router()


#Start
@router.message(CommandStart)
async def start(message:types.Message):
    data = {
        "username": message.from_user.id,
        "password": message.from_user.id,
        "email": f"user{str(message.from_user.id)}@example.com",
        "first_name": message.from_user.username,
        "last_name": message.from_user.first_name
        }
    res = await register(data)
    
    await message.answer('''
        Здравствуйте! 👋\n\n
        Вы успешно зарегистрировались,\n
        переходите на сайт\n\n
        👇''' , reply_markup=inl_site)
