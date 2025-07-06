from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ʙɪɴɢ ᴄʜᴀᴛ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙɪɴɢ ᴄʜᴀᴛ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ʙɪɴɢ</code>
    ᴅᴀᴘᴀᴛ ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏʀᴍᴀꜱɪ ᴛᴇʀʙᴀʀᴜ ᴅᴀʀɪ ᴡᴇʙ, ᴍᴇᴍʙᴀɴᴛᴜ ᴅᴇɴɢᴀɴ ᴛᴜɢᴀs ᴘʀᴏᴅᴜᴋᴛɪᴠɪᴛᴀs, ꜱᴇᴘᴇʀᴛɪ ᴍᴇᴍʙᴜᴀᴛ ᴅᴀꜰᴛᴀʀ, ᴍᴇɴɢᴀᴛᴜʀ ᴊᴀᴅᴡᴀʟ, ʙɪꜱᴀ ᴍᴇʀᴇᴋᴏᴍᴇɴᴅᴀꜱɪᴋᴀɴ: ᴡɪꜱᴀᴛᴀ, ʙᴜᴋᴜ, ꜰɪʟᴍ ᴅʟʟ</b></blockquote>
"""


@PY.UBOT("bing")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ : .ʙᴀʀᴅ ǫᴜᴇʀʏ"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5469745532693923461>♾</emoji>ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/bing-chat?text={a}&apikey=045705b1')

            try:
                if "message" in response.json():
                    x = response.json()["message"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ 'ʀᴇsᴜʟᴛs' ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴅɪ ʀᴇsᴘᴏɴꜱ.")
            except KeyError:
                await message.reply_text("ᴋᴇsᴀʟᴀʜᴀɴ ᴀᴋsᴇs ʀᴇsᴘᴏɴꜱ.")
    except Exception as e:
        await message.reply_text(f"ᴋᴇsᴀʟᴀʜᴀɴ: {e}")
