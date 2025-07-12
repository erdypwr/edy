from pyrogram import Client, filters
import requests
from PyroUbot import *

__MODULE__ = "ᴛᴇʀᴀʙᴏx"
__HELP__ = """
<blockquote> <b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇʀᴀʙᴏx ᴄᴇꜱꜱ 』

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}terabox</code> terabox <b>[link nya]</b>
ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ᴛᴇʀᴀʙᴏx.</b></blockquote>

"""

@PY.UBOT("terabox")
async def terabox_handler(client, message):
    if len(message.command) < 2:
        await message.reply_text("ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ᴄᴏɴᴛᴏʜ: .ᴛᴇʀᴀʙᴏx ʟɪɴᴋ ᴠɪᴅɪᴇᴏ <ᴜʀʟ>")
        return
    
    url = message.command[1]
    api_url = f"https://api.botcahx.eu.org/api/download/terabox?url={url}&apikey=045705b1"
    response = requests.get(api_url)
    
    if response.status_code != 200:
        await message.reply_text("ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴛᴇʀᴀʙᴏx ᴀᴘɪ ᴄᴜᴋɪ.")
        return
    
    data = response.json()
    if not data.get("status"):
        await message.reply_text("ᴛᴇʀᴀʙᴏx ᴀᴘɪ ᴍᴇɴɢᴇᴍʙᴀʟɪᴋᴀɴ ʀᴇꜱᴘᴏɴꜱ ɢᴀɢᴀʟ ᴄᴜᴋɪ.")
        return
    
    result_text = "📂 **ᴅᴀꜰᴛᴀʀ ꜰɪʟᴇ ᴛᴇʀᴀʙᴏx:**\n\n"
    for item in data.get("result", []):
        name = item.get("name", "ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")
        created = item.get("created", "ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")
        files = item.get("files", [])
        
        result_text += f"📁 **{name}** (ᴅɪʙᴜᴀᴛ: {created})\n"
        for file in files:
            filename = file.get("filename", "ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")
            size = file.get("size", "ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")
            url = file.get("url", "ᴛɪᴅᴀᴋ ᴛᴇʀꜱᴇᴅɪᴀ")
            result_text += f"  ├ 🎬 {filename} ({size} bytes)\n  └ 🔗 [ᴅᴏᴡɴʟᴏᴀᴅ]({url})\n\n"
    
    await message.reply_text(result_text, disable_web_page_preview=True)
