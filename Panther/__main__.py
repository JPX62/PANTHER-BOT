
from pyrogram import idle, Client, filters
from config import PREFIX
from Panther import app, LOGGER
import logging
from Panther.modules import *

app.start()
me = app.get_me()
print(f"Panther UserBot started for user {me.id}. Type {PREFIX}help in any telegram chat.")
idle()
