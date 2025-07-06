from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴀɪ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɪ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴀɪ</code>
ʙᴜᴀᴛ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴄᴏɴᴛᴏʜ <code>{0}ᴀɪ</code> ʜᴀʟᴏ</b></blockquote>
"""

@PY.UBOT("ai")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ : .ᴀɪ ʜᴀʟᴏ"
            )
        else:
            prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji>ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/openai-chat?text={a}&apikey=045705b1')

            try:
                if "message" in response.json():
                    x = response.json()["message"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ 'ʀᴇꜱᴜʟᴛꜱ' ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴅɪ ʀᴇꜱᴘᴏɴꜱ.")
            except KeyError:
                await message.reply_text("ᴋᴇꜱᴀʟᴀʜᴀɴ ᴀᴋꜱᴇꜱ ʀᴇꜱᴘᴏɴꜱ.")
    except Exception as e:
        await message.reply_text(f"{e}")
        
        
@PY.BOT("ai")
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ : .ᴀɪ ʜᴀʟᴏ"
            )
        else:
            prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji>ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/openai-chat?text={a}&apikey=045705b1')

            try:
                if "message" in response.json():
                    x = response.json()["message"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ 'ʀᴇꜱᴜʟᴛꜱ' ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴅɪ ʀᴇꜱᴘᴏɴꜱ.")
            except KeyError:
                await message.reply_text("ᴋᴇꜱᴀʟᴀʜᴀɴ ᴀᴋꜱᴇꜱ ʀᴇꜱᴘᴏɴꜱ.")
    except Exception as e:
        await message.reply_text(f"{e}")
