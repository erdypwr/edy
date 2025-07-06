from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴋᴏᴅᴇ ᴘᴏs"
__HELP__ = """
<blockquote><b>Bantuan Untuk Kode Pos Desa Cess</b>

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}kdps</code>
    dapat Membantu Melihat Kode Pos Suatu Desa Cess</b></blockquote>
"""


@PY.UBOT("kdps")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>Mohon Gunakan Format\nContoh : .kdps nama desa"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5319230516929502602>🔍</emoji>Mencari Cess....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/kodepos?query={a}&apikey=045705b1')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("Tidak Ditemukan Kunci 'hasil' Dalam Respons Cess.")
            except KeyError:
                await message.reply_text("Error Mengakses Respons Cess.")
    except Exception as e:
        await message.reply_text(f"{e}")
