from aiogram import types

from keyboards.default import kb_test
from loader import dp


@dp.message_handler(text='biror bir matn')
async def test(message: types.Message):
    await message.answer(f"Kechirasiz , {message.from_user.full_name}!\n"
                         f"Iltimos, matnni tanlang ",reply_markup=kb_test)