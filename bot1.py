from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='1668821288:AAHzQ7WlvWTpfL3SHKw7XeChMaGXsIxSDwo')
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = 'привед'
    sent_message = await bot.send_message(chat_id=chat_id, text=text)
    print(sent_message.to_python())
    sent_message = await bot.send_photo(chat_id=chat_id, photo=open("pil-basic-example.png", "rb"))
    print(sent_message.photo[-1]['file_unique_id'])
    # result = await bot.set_chat_title(chat_id=chat_id, title='new title')
    # invite_link = await bot.export_chat_invite_link(chat_id=chat_id)
    bot_user = await bot.get_me()
    sent_message = await bot.send_message(chat_id=chat_id, text=bot_user)
    print(bot_user.username)
executor.start_polling(dp)
