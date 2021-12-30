
import asyncio

from pyrogram import idle
from panther import panther
from panther.plugins import *
from panther.core.startup_checks import check_or_set_log_channel, check_arq_api
from panther.core.panther_database.panther_conf import get_log_channel
from config import Config


async def main_startup():
    print("""
|| Panther Userbot ||

Copyright (c) 2021 kaal0408
"""
    )
    await panther.start()
    log_channel_id = await check_or_set_log_channel()
    await check_arq_api()
    try:
        await panther.send_message(chat_id=log_channel_id[1], text="`panther Userbot is started!`")
    except:
        print("WARNING: There was an error while creating the LOG CHANNEL please add a one manually!")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main_startup())
