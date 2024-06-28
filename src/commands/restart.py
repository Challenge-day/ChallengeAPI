from aiogram import types

restart_flag = False

async def restart_command(message: types.Message):
    global restart_flag
    restart_flag = True
    await message.answer("Bot is restarting...")


   