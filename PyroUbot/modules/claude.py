from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴄʟᴀᴜᴅᴇ ᴀɪ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄʟᴀᴜᴅᴇ ᴄᴇꜱꜱ 』

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴄʟᴀᴜᴅᴇ</code>
    ᴛᴜʟɪs ᴘᴇʀᴄᴀᴋᴀᴘᴀɴ ᴅᴇɴɢᴀɴ ᴄʟᴀᴜᴅᴇ. ᴄᴏɴᴛᴏʜ: <code>{0}ᴄʟᴀᴜᴅᴇ</code> ʜᴀɪ</b></blockquote>

"""

@PY.UBOT("claude")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ ʏᴀɴɢ ʙᴇɴᴀʀ\nᴄᴏɴᴛᴏʜ : .ᴄʟᴀᴜᴅᴇ ʜᴀɪ"
            )
        else:
            prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji>ᴍᴇɴᴊᴀᴡᴀʙ ᴄᴇꜱꜱ....")
            hai = message.text.split(' ', 1)[1]
            response = requests.get(f'https://vapis.my.id/api/claude?q={hai}')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ ʜᴀsɪʟ ᴅɪ ʀᴇsᴘᴏɴs ᴄᴜᴋɪ!.")
            except KeyError:
                await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ sᴀᴀᴛ ᴍᴇɴɢᴀᴋsᴇs ʀᴇsᴘᴏɴs ᴄᴜᴋɪ!.")
    except Exception as e:
        await message.reply_text(f"{e}")
      
