import random
from pyrogram import *
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴄᴇᴋ ᴋᴇᴄᴀɴᴛɪᴋᴀɴ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴋᴇᴄᴀɴᴛɪᴋᴀɴ ᴄᴇꜱꜱ 』

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}ᴄᴇᴋᴋᴄᴛᴋɴ [ɴᴀᴍᴀ]</code> → ʀᴀᴛɪɴɢ ʙᴇʀᴀᴘᴀ ᴘᴇʀꜱᴇɴ ᴋᴇᴄᴀɴᴛɪᴋᴀɴ ɴᴀᴍᴀ  

ꜱᴜᴍʙᴇʀ: ʀᴀɴᴅᴏᴍ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴇʀᴅᴀꜱᴀʀᴋᴀɴ ɴᴀᴍᴀ.</b></blockquote>

"""

KHODAM_LIST = [
    "1% (ᴊᴇʟᴇᴋ ʙɪɴɢɪᴛ)🤮", "55% (ᴍᴀʏᴀɴ)🙂", "30% (ᴅᴇᴍᴘᴜʟ)🙃", "70% (ᴄᴀɴᴛɪᴋ ᴛᴀᴘɪ ᴀɢᴀᴋ ɪʀᴇɴɢ)😉",
    "90% (ᴄᴀɴᴛɪᴋɴʏᴀ ᴘᴀꜱ)😎", "100% (ᴄᴀɴᴛɪᴋ+ᴛᴏʙʀᴜᴛ)🤯", "4% (ɪʀᴇɴɢ)🤢", "10% (ɪʀᴇɴɢ+ᴛᴇᴘᴏꜱ)😖", "1000% (ᴄᴀɴᴛɪᴋ+ᴛᴏʙʀᴜᴛ+ᴍᴀɴɪꜱ)😱"
]

@PY.UBOT("cekkctkn")
@PY.TOP_CMD
async def cek_khodam(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return await message.reply_text("⚠️ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: ᴄᴇᴋᴋᴄᴛᴋɴ [ɴᴀᴍᴀ]")

    nama = args[1]
    khodam = random.choice(KHODAM_LIST)
    hasil = f"<blockquote><b>🤭ʜᴀꜱɪʟ ᴋᴇᴄᴀɴᴛɪᴋᴀɴ🤭\n\n=👩 ɴᴀᴍᴀ: `{nama}`\n ᴘᴇʀꜱᴇɴ: `{khodam}`</blockquote></b>"
    await message.reply_text(hasil)