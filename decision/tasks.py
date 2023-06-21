from celery import shared_task
from pyrogram import Client
from django.conf import settings
from bot.utils import RunningBot



# @job
# def message(telegram_user,txt):
#     bot_settings = settings.PYROGRAM_BOT
#     running_bot = RunningBot()
#     running_bot_data = running_bot.read_data()

#     if running_bot_data is None:
#         return
#     with Client(
#         name=f"{bot_settings['BOT_NAME']}",
#         session_string=running_bot_data["session_string"],
#         no_updates=True,
#         workers=1,
#         ) as app:
#             app.send_message(chat_id=telegram_user,text=txt)
@shared_task
def message(telegram_user,txt):
    bot_settings = settings.PYROGRAM_BOT
    running_bot = RunningBot()
    running_bot_data = running_bot.read_data()

    if running_bot_data is None:
        return
    with Client(
        name=f"{bot_settings['BOT_NAME']}",
        session_string=running_bot_data["session_string"],
        no_updates=True,
        workers=1,
        ) as app:
            app.send_message(chat_id=telegram_user,text=txt)
