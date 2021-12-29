
import asyncio
import tgcrypto
from pyrogram import Client

print("""
|| Panther Userbot ||

Copyright (c) 2021 kaal0408
""")

async def pyro_str():
    print("\nPlease Enter All Required Values to Generate Pyrogram String Session for your Account! \n")
    api_id = int(input("Enter Your APP ID: "))
    api_hash = input("Enter Your API HASH: ")
    async with Client(":memory:", api_id, api_hash) as PantherUB:
        pyro_session = await PantherUB.export_session_string()
        session_msg = await PantherUB.send_message("me", f"`{pyro_session}`")
        await session_msg.reply_text("Successfully Generated String Session! Thanks for trying [Panther Userbot](https://github.com/kaal0408/Panther) \n\n**Join @Panthersupport**", disable_web_page_preview=True)
        print("\nString Session has been sent to your saved messages. Please check it. Thank You!\n")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(pyro_str())
