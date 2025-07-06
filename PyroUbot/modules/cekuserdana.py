from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴜsᴇʀ ᴅᴀɴᴀ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄʜᴇᴄᴋ ᴜsᴇʀɴᴀᴍᴇ ᴅᴀɴᴀ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}checkdana</code>
ᴄᴇᴋ ᴜsᴇʀɴᴀᴍᴇ ᴅᴀɴᴀ ᴅᴀʀɪ ɴᴏᴍᴏʀ ᴄᴏɴᴛᴏʜ <code>{0}checkdana</code> 085xxxx</b></blockquote>
"""

@PY.UBOT("checkdana")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ : .ᴄʜᴇᴄᴋᴅᴀɴᴀ 085xxx"
            )
        else:
            prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji>ᴘʀᴏsᴇss ᴄᴇss....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.siputzx.my.id/api/check/dana?account_number={a}')

            try:
                if "data" in response.json():
                    x = response.json()["data"]                  
                    await prs.edit(
                      f"<blockquote>ʙᴇʀɪᴋᴜᴛ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴘᴀʏᴍᴇɴᴛ ᴅᴀɴᴀ ᴇʟᴜ{x}</blockquote>"
                    )
                else:
                    await message.reply_text("ɴᴏ 'results' ᴋᴇʏ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ.")
            except KeyError:
                await message.reply_text("ᴇʀʀᴏʀ ᴀᴄᴄᴇssɪɴɢ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ.")
    except Exception as e:
        await message.reply_text(f"{e}")
