import random
from pyrogram import *
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴄᴇᴋ ᴋᴇᴛᴀᴍᴘᴀɴᴀɴ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴋᴇᴛᴀᴍᴘᴀɴᴀɴ</b>

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}cektmpn [nama]</code> → ʀᴀᴛᴛɪɴɢ ʙᴇʀᴀᴘᴀ ᴘᴇʀsᴇɴ ᴋᴇᴛᴀᴍᴘᴀɴᴀɴ ɴᴀᴍᴀ  

sᴜᴍʙᴇʀ: ʀᴀɴᴅᴏᴍ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ɴᴀᴍᴀ.</blockquote></b>
"""

KHODAM_LIST = [
    "1%🤮", "55%🙂", "30%🙃", "70%😉",
    "90%😎", "100%🤯", "4%🤢", "10%😖", "1000%😱"
]

@PY.UBOT("cektmpn")
@PY.TOP_CMD
async def cek_khodam(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return await message.reply_text("⚠️ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: ᴄᴇᴋᴛᴍᴘɴ [ɴᴀᴍᴀ]")

    nama = args[1]
    khodam = random.choice(KHODAM_LIST)
    hasil = f"<blockquote><b>🤭ʜᴀsɪʟ ᴋᴇᴛᴀᴍᴘᴀɴᴀɴ🤭\n\n🧑 ɴᴀᴍᴀ: `{nama}`\n ᴘᴇʀsᴇɴ: `{khodam}`</blockquote></b>"
    await message.reply_text(hasil)