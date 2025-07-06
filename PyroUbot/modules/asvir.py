from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴀsᴠɪʀ ᴀɪ"
__HELP__ = """
<blockquote><b>✮ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀsɪsᴛᴇɴ ᴠɪʀᴛᴜᴀʟ ✮

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴀsᴠɪʀ</code>
    ᴀɪ ʙɪsᴀ ᴅɪɢᴜɴᴀᴋᴀɴ ᴜɴᴛᴜᴋ: ᴛʀᴀɴsʟᴀᴛᴇ, ᴍᴇᴍʙᴇʀɪᴋᴀɴ sᴀʀᴀɴ, ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ , ᴄᴏɴᴛᴏʜ <code>{0}ᴀsᴠɪʀ</code> ʙᴀʜᴀsᴀ ɪɴɢɢʀɪs ɴʏᴀ 'sɪᴀᴘᴀ ᴋᴀᴍᴜ' ɪᴛᴜ ᴀᴘᴀ?</b></blockquote>
"""

@PY.UBOT("asvir")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ : .ᴀsᴠɪʀ ʙᴀʜᴀsᴀ ɪɴɢɢʀɪs ɴʏᴀ 'sɪᴀᴘᴀ ᴋᴀᴍᴜ' ɪᴛᴜ ᴀᴘᴀ?"
            )
        else:
            prs = await message.reply_text(f"<emoji id=4943239162758169437>🤩</emoji>ᴍᴇɴᴊᴀᴡᴀʙ....")
            hai = message.text.split(' ', 1)[1]
            response = requests.get(f'https://vapis.my.id/api/llamav1?q={hai}')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ 'ʀᴇsᴜʟᴛs' ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴅɪ ʀᴇsᴘᴏɴꜱ.")
            except KeyError:
                await message.reply_text("ᴋᴇsᴀʟᴀʜᴀɴ ᴀᴋsᴇs ʀᴇsᴘᴏɴꜱ.")
    except Exception as e:
        await message.reply_text(f"ᴋᴇsᴀʟᴀʜᴀɴ: {e}")
      
