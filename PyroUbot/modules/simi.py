from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "sɪᴍɪ ᴀɪ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Simi AI Cess

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}simi</code>
    Dapat Mengobrol, Tapi Agak Toxic Cuki</b></blockquote>
"""


@PY.UBOT("simi")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>Mohon Gunakan Format Cuki\nContoh : .simi query"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5319230516929502602>🔍</emoji>Menjawab Cess....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/simsimi?query={a}&apikey=Boyy')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("Tidak Ditemukan Kunci 'hasil' Dalam Respons Cess.")
            except KeyError:
                await message.reply_text("Kesalahan Saat Mengakses Respons Cess.")
    except Exception as e:
        await message.reply_text(f"{e}")
