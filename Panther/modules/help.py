
from pyrogram import filters
from Panther import app, HELP, CMD_HELP
from config import PREFIX
from Panther.helpers.pyrohelper import get_arg

HELP.update(
    {
        "**Admin Tools**": "__ban, unban, promote, demote, kick, mute, unmute, gmute, ungmute, pin, purge, del, invite__",
        "**AFK**": "__afk, unafk__",
        "**Alive**": "__alive, ping__",
        "**Developer**": "__eval, term__",
        "**Filters**": "__filter, filters, stop, stopall__",
        "**Misc**": "__paste, tr, whois, id__",
        "**Notes**": "__save, get, clear, clearall, notes__",
        "**Anti-PM**": "__pmguard, setpmmsg, setlimit, setblockmsg, allow, deny__",
        "**Sticker**": "__kang, stkrinfo__",
        "**Greetings**": "__setwelcome, clearwelcome__",
        "**Updater**": "__update__",
    }
)


@app.on_message(filters.command("help", PREFIX) & filters.me)
async def help(client, message):
    args = get_arg(message)
    if not args:
        text = "**Available Commands**\n\n"
        for key, value in HELP.items():
            text += f"{key}: {value}\n\n"
        await message.edit(text)
        return
    else:
        module_help = CMD_HELP.get(args, False)
        if not module_help:
            await message.edit("__Invalid module name specified.__")
            return
        else:
            await message.edit(module_help)

@app_on_cmd(
    ["help", "helper"],
    cmd_help={
        "help": "Gets Help Menu",
        "example": "{ch}help",
    },
)
async def help(client, message):
    engine = message.Engine
    f_ = await edit_or_reply(message, engine.get_string("PROCESSING"))
    if bot:
        starkbot = bot.me
        bot_username = starkbot.username
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="help")
            await client.send_inline_bot_result(
                message.chat.id, nice.query_id, nice.results[0].id, hide_via=True
            )
        except BaseException as e:
            return await f_.edit(engine.get_string("HELP_OPEN_ERROR").format(e))
        await f_.delete()
    else:
        cmd_ = get_text(message)
        if not cmd_:
            help_t = prepare_cmd_list(engine)            
            await f_.edit(help_t)
        else:
            help_s = get_help_str(cmd_)
            if not help_s:
                await f_.edit(engine.get_string("PLUGIN_NOT_FOUND"))
                return
            await f_.edit(help_s)
