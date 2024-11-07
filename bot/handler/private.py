import django, os
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from asgiref.sync import sync_to_async
from main.models import UserMod


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
user_private_router = Router()
dp = user_private_router


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    await sync_to_async(UserMod.objects.create)(
        user_id = message.from_user.id,
        user_name = message.from_user.full_name
    )
    read = await sync_to_async(UserMod.objects.filter(user_id=message.from_user.id).first)()
    
    # read.user_name = 'new name'
    # await sync_to_async(read.delete)()
    # await sync_to_async(read.save)()

    await message.answer(f'{read.user_id} {read.user_name}')
