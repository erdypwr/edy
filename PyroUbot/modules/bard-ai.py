from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ʙᴀʀᴅ ᴀɪ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙᴀʀᴅ-ᴀɪ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ʙᴀʀᴅ</code>
    ᴅᴀᴘᴀᴛ ᴍᴇɴᴜʟɪs ᴄᴇʀɪᴛᴀ, ᴘᴜɪsɪ, sᴋʀɪᴘ, ᴋᴏᴅᴇ ᴋᴏᴍᴘᴜᴛᴇʀ, ᴍᴜsɪᴋ, ᴇᴍᴀɪʟ, sᴜʀᴀᴛ, ᴅʟʟ</b></blockquote>
"""


@PY.UBOT("bard")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ : .ʙᴀʀᴅ ǫᴜᴇʀʏ"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5319230516929502602>🔍</emoji>ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.betabotz.eu.org/api/search/bard-ai?text={a}&apikey=Btz-bxwol')

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
