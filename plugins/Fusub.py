from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FUB_TEXT ="""<b><blockquote>Force Subscription Management
<i>Set, manage, or clear force subscribe channels.</i></blockquote>

‣ /setchat1 - <i>Set force subscribe channel - /setchat1 channel_id (Answer the questions after that) Bot must be admin of that channel (Bot will create a new invite link)</i>
‣ /setchat2 - <i>Set force subscribe channel - /setchat2 channel_id (Answer the questions after that) Bot must be admin of that channel (Bot will create a new invite link)</i>
‣ /delchat1 - <i>delete Force subscribe channel</i>
‣ /delchat2 - <i>delete Force subscribe channel</i>
‣ /viewchat1 - <i>Check invite link for force subscribe channel</i>
‣ /viewchat2 - <i>Check invite link for force subscribe channel</i>
‣ /purge_one - <i>Clear all force subscribe users from db</i>
‣ /purge_two - <i>Clear all force subscribe users from db</i>
‣ /totalreq - <i>Total all force subscribe Count</i></b>"""

@Client.on_message(filters.command("fusub"))
async def generate_link(client, message):
    command_text = message.text.split(maxsplit=1)
    if len(command_text) < 2:
        await message.reply(FUB_TEXT)
        return
