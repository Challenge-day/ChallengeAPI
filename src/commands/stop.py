from aiogram import types

stop_flag = False

async def stop_command(message: types.Message):
    global stop_flag
    stop_flag = True
    await message.answer("Bot is stopping...")

