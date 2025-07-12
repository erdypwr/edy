from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ꜱɪᴍɪ ᴀɪ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱɪᴍɪ ᴀɪ ᴄᴇꜱꜱ 』

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ꜱɪᴍɪ</code>
    ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴏʙʀᴏʟ, ᴛᴀᴘɪ ᴀɢᴀᴋ ᴛᴏxɪᴄ ᴄᴜᴋɪ</b></blockquote>
"""


@PY.UBOT("simi")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ ᴄᴜᴋɪ\nᴄᴏɴᴛᴏʜ : .ꜱɪᴍɪ ǫᴜᴇʀʏ"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5319230516929502602>🔍</emoji>ᴍᴇɴᴊᴀᴡᴀʙ ᴄᴇꜱꜱ....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/simsimi?query={a}&apikey=Boyy')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴋᴜɴᴄɪ 'ʜᴀꜱɪʟ' ᴅᴀʟᴀᴍ ʀᴇꜱᴘᴏɴꜱ ᴄᴜᴋɪ ᴄᴇꜱꜱ.")
            except KeyError:
                await message.reply_text("ᴋᴇꜱᴀʟᴀʜᴀɴ ꜱᴀᴀᴛ ᴍᴇɴɢᴀᴋꜱᴇꜱ ʀᴇꜱᴘᴏɴꜱ ᴄᴇꜱꜱ.")
    except Exception as e:
        await message.reply_text(f"{e}")
