import random
from pyrogram import *
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴄᴇᴋ ᴀɢᴀᴍᴀ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴀɢᴀᴍᴀ ᴄᴇꜱꜱ 』

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}ᴄᴇᴋᴀɢᴀᴍᴀ [ɴᴀᴍᴀ]</code> → ᴅᴇᴛᴇᴋꜱɪ ᴀɢᴀᴍᴀ ᴅᴀʀɪ ɴᴀᴍᴀ  

ꜱᴜᴍʙᴇʀ: ʀᴀɴᴅᴏᴍ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴇʀᴅᴀꜱᴀʀᴋᴀɴ ɴᴀᴍᴀ.</blockquote></b>

"""

AGAMA_LIST = [
    "ʜɪɴᴅᴜ","ᴀᴛᴇɪꜱ (ɢᴀᴋ ᴘᴜɴʏᴀ ᴀɢᴀᴍᴀ","ɪꜱʟᴀᴍ","ᴋʀɪꜱᴛᴇɴ","ʙᴜᴅʜᴀ","ᴋᴀᴛᴏʟɪᴋ","ᴋʀɪꜱᴛᴇɴ ᴘʀᴏᴛᴇꜱᴛᴀɴ","ɪꜱʟᴀᴍ ᴋᴛᴘ","ᴋᴏɴɢʜᴜᴄᴜ",
]

@PY.UBOT("cekagama")
@PY.TOP_CMD
async def cek_agama(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return await message.reply_text("<blockquote><b>⚠️ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: .ᴄᴇᴋᴀɢᴀᴍᴀ [ɴᴀᴍᴀ]</blockquote></b>")

    nama = args[1]
    agama = random.choice(AGAMA_LIST)
    hasil = f'''<blockquote><b>
    ʜᴀꜱɪʟ ᴅᴇᴛᴇᴋꜱɪ ᴀɢᴀᴍᴀ ᴅᴀʀɪ {nama}
    ╭───────────────────────
    ├ ɴᴀᴍᴀ : `{nama}`
    ├ ᴀɢᴀᴍᴀ: `{agama}`
    ├ ꜱᴇʟᴀᴍᴀᴛ ʏᴀ ᴀɢᴀᴍᴀ ɴʏᴀ ᴄᴏᴄᴏᴋ ᴋᴏᴋ
    ╰────────────────────────
    ɴᴏᴛᴇ ᴍᴀᴀғ ʏᴀ {nama} ᴄᴜᴍᴀ ʙᴇᴄᴇʟᴜ ᴋᴏᴋ 😁
    
    </blockquote></b>'''
    await message.reply_text(hasil)
