from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴛᴜʀʙᴏ ɢᴘᴛ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴜʀʙᴏ ɢᴘᴛ ᴄᴇꜱꜱ 』

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}turbo</code>
    ᴋᴇᴛɪᴋ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴋᴀᴍᴜ ᴅɪꜱɪɴɪ, ᴄᴏɴᴛᴏʜ: <code>{0}turbo ʜᴀɪ ᴀᴘᴀ ᴋᴀʙᴀʀ?</code></b></blockquote>
"""

@PY.UBOT("turbo")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>ᴍᴏʜᴏɴ ᴋᴇᴛɪᴋ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴅᴇɴɢᴀɴ ꜰᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ : .turbo ʜᴀɪ ᴀᴘᴀ ᴋᴀʙᴀʀ?"
            )
        else:
            prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji>ᴛᴜʀʙᴏ ꜱᴇᴅᴀɴɢ ᴍᴇɴᴊᴀᴡᴀʙ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴇʟᴜ....")
            hai = message.text.split(' ', 1)[1]
            response = requests.get(f'https://vapis.my.id/api/turbov1?q={hai}')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("ᴇʀʀᴏʀ, ᴊᴀᴡᴀʙᴀɴ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴅᴀʀɪ ᴀᴘɪ.")
            except KeyError:
                await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ ᴍᴇɴɢᴀᴍʙɪʟ ᴊᴀᴡᴀʙᴀɴ ᴅᴀʀɪ ᴀᴘɪ.")
    except Exception as e:
        await message.reply_text(f"{e}")
      
