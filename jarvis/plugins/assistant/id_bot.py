from telethon.utils import pack_bot_file_id
from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd
from jarvis import bot
from telethon import events, custom, Button
from telethon.tl.types import (
    Channel,
    Chat,
    User
)

import emoji
import asyncio
from googletrans import Translator
import re
import io
from math import ceil
from jarvis.plugins import inlinestats
from telethon import custom, events, Button
from jarvis import CMD_LIST
from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd
from telethon.utils import get_display_name
from jarvis.utils import admin_cmd, sudo_cmd
from jarvis.uniborgConfig import Config
from telethon import events
from datetime import datetime
from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd
import time
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from jarvis import Lastupdate, bot
from jarvis.plugins.sql_helper.botusers_sql import add_me_in_db, his_userid
from jarvis.plugins.sql_helper.idadder_sql import add_usersid_in_db, get_all_users

@tgbot.on(events.NewMessage(pattern="^/id"))
async def _(event):
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await tgbot.send_message(
                event.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id), bot_api_file_id
                )
            )
        else:
            await tgbot.send_message(
                event.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id)
                )
            )
    else:
        await tgbot.send_message(event.chat_id, "Current Chat ID: `{}`".format(str(event.chat_id)))
