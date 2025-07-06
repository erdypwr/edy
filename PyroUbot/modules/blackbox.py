from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ʙʟᴀᴄᴋʙᴏx ᴀɪ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʟᴀᴄᴋʙᴏx ᴀɪ ⦫</b>

<blockquote><b>⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}ʙʟᴀᴄᴋʙᴏx</code>
⊷ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴇʟᴜ ᴅᴇɴɢᴀɴ ʙᴇʀʙᴀɢᴀɪ ᴋᴏɴsᴇᴘ ᴘᴇᴍᴘʀᴏɢʀᴀᴍᴀɴ</b></blockquote>
"""


@PY.UBOT("blackbox")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ : .ʙʟᴀᴄᴋʙᴏx ǫᴜᴇʀʏ"
            )
        else:
            prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji>ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/blackbox-chat?text={a}&apikey=045705b1')

            try:
                if "message" in response.json():
                    x = response.json()["message"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ ʀᴇsᴜʟᴛ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴅᴀʟᴀᴍ ʀᴇsᴘᴏɴꜱ.")
            except KeyError:
                await message.reply_text("ᴋᴇsᴀʟᴀʜᴀɴ ᴀᴋsᴇs ʀᴇsᴘᴏɴꜱ.")
    except Exception as e:
        await message.reply_text(f"ᴋᴇsᴀʟᴀʜᴀɴ: {e}")
