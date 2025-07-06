import random
from pyrogram import *
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴄᴇᴋ ᴋʜᴏᴅᴀᴍ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴋʜᴏᴅᴀᴍ 』

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}ᴄᴇᴋᴋʜᴏᴅᴀᴍ [ɴᴀᴍᴀ]</code> → ᴍᴇʟɪʜᴀᴛ ᴊᴇɴɪꜱ ᴋʜᴏᴅᴀᴍ ʙᴇʀᴅᴀꜱᴀʀᴋᴀɴ ɴᴀᴍᴀ  

ꜱᴜᴍʙᴇʀ: ʀᴀɴᴅᴏᴍ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴇʀᴅᴀꜱᴀʀᴋᴀɴ ɴᴀᴍᴀ.</b></blockquote>

"""

KHODAM_LIST = [
    "🐉 ɴᴀɢᴀ ᴇᴍᴀꜱ", "🔥 ᴍᴀᴄᴀɴ ᴘᴜᴛɪʜ", "🌊 ꜱɪʟᴜᴍᴀɴ ᴀɪʀ", "🦅 ɢᴀʀᴜᴅᴀ ꜱᴀᴋᴛɪ",
    "⚡ ʜᴀʀɪᴍᴀᴜ ᴘᴇᴛɪʀ", "🌓 ᴊɪɴ ᴘᴇɴᴊᴀɢᴀ", "🌿 ʀᴏʜ ᴀʟᴀᴍ", "🪨 ʙᴀᴛᴜ ʙᴇʀᴛᴜᴀʜ", "🖕 ᴋᴏɴᴛᴏʟ ᴘᴜᴋɪɴᴀᴋ", "👽 ᴀʟɪᴇɴ ɴɢᴏᴄᴏᴋ", " ꜱᴀɴᴅᴀʟ ᴊᴇᴘɪᴛ", " ᴊɪɴ ᴄᴏᴋʟᴀᴛ ʙᴀᴛᴀɴɢᴀɴ", " ʙᴀᴛᴜ ʙᴀᴛᴀ", "ᴋᴀɴᴄɪɴɢ ʙᴀᴊᴜ", " ᴇꜱ ᴋʀɪᴍ", " ᴋᴇᴛᴏᴘʀᴀᴋ ", " ꜱᴏᴛᴏ ᴍᴀᴅᴜʀᴀ", "ʀᴇᴍᴏᴛ ᴛᴠ", "ᴋɴᴀʟᴘᴏᴛ ʀᴀᴄɪɴɢ", "ʙɪʜᴜɴ", "ᴋᴜʏᴀɴɢ", "ɴʏɪ ʙʟᴏʀᴏɴɢ", "ꜱᴀᴛᴘᴀᴍ ᴋᴏᴍᴘʟᴇᴋ", "ᴛᴜꜱᴜᴋ ꜱᴀᴛᴇ", "ᴛᴜᴛᴜᴘ ᴏᴅᴏʟ", "ʙᴇʙᴇᴋ ꜱᴜᴍʙɪɴɢ", "ꜱᴀᴘɪ ꜱᴜᴍʙɪɴɢ", "ᴜʟᴛʀᴀᴍᴀɴ ᴘɪɴᴋ", "ꜱᴀʙᴜɴ ʙᴏʟᴏɴɢ", "ᴛᴀɪ ᴀʏᴀᴍ", "ʙᴜʀᴜɴɢ ᴘᴜʏᴜʜ", "ʀᴏᴛɪ ᴀᴏᴋᴀ"
]

@PY.UBOT("cekkhodam")
@PY.TOP_CMD
async def cek_khodam(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return await message.reply_text("⚠️ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: ᴄᴇᴋᴋʜᴏᴅᴀᴍ [ɴᴀᴍᴀ]")

    nama = args[1]
    khodam = random.choice(KHODAM_LIST)
    hasil = f"<blockquote><b>🔮 **ʜᴀꜱɪʟ ᴄᴇᴋ ᴋʜᴏᴅᴀᴍ** 🔮\n\n🧑 ɴᴀᴍᴀ: `{nama}`\n🪄 ᴋʜᴏᴅᴀᴍ: `{khodam}`</blockquote></b>"
    await message.reply_text(hasil)