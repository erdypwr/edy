from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

__MODULE__ = "ʀᴀɴᴅᴏᴍ ᴋᴜᴄɪɴɢ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜰᴏᴛᴏ ʀᴀɴᴅᴏᴍ ᴋᴜᴄɪɴɢ ᴄᴇꜱꜱ 』</b>

<b>⌲ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ʀᴀɴᴅᴏᴍ [ᴋᴜᴄɪɴɢ]</code></b></blockquote>
"""

URLS = {
    "kucing": "https://api.siputzx.my.id/api/r/cats"
}

@PY.UBOT("random")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"Query Tidak Valid Cess. Gunakan Salah Satu Dari: {valid_queries}.")
        return

    processing_msg = await message.reply("Prosess Cess...")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"Gagal Mengambil Gambar Cecan Error Cess: {e}")
