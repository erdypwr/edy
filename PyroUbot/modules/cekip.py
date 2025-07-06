import socket
from pyrogram import *
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴄᴇᴋ ɪᴘ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴇᴋ ɪᴘ ᴡᴇʙꜱɪᴛᴇ ᴄᴇꜱꜱ 』

ᴘᴇʀɪɴᴛᴀʜ: <code>{0}ᴄᴇᴋɪᴘ</code> [ᴅᴏᴍᴀɪɴ]
ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴀʟᴀᴍᴀᴛ ɪᴘ ᴅᴀʀɪ ᴅᴏᴍᴀɪɴ ʏᴀɴɢ ᴅɪʙᴇʀɪᴋᴀɴ</b></blockquote>

"""

@PY.UBOT("cekip")
@PY.TOP_CMD
async def cek_ip_command(client, message):
    # Ambil argumen dari pesan
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        await message.reply_text(
            "<blockquote><b>⚠️ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: ᴄᴇᴋɪᴘ [ᴅᴏᴍᴀɪɴ]</b></blockquote>"
        )
        return

    domain = args[1]

    try:
        ip_address = socket.gethostbyname(domain)
        result_text = f"<blockquote><b>🔍 **ʜᴀꜱɪʟ ᴘᴇɴɢᴇᴄᴇᴋᴀɴ ɪᴘ ᴜɴᴛᴜᴋ:** `{domain}`\n\n🌐 ɪᴘ ᴀᴅᴅʀᴇꜱꜱ: `{ip_address}`</b></blockquote>"
    except Exception as e:
        result_text = f"❌ ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ: {str(e)}"

    await message.reply_text(result_text)