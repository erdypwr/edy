import aiohttp
import filetype
import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot import *

__MODULE__ = "ᴡʜᴀᴛ ᴍᴜsɪᴄ"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴡʜᴀᴛ ᴍᴜꜱɪᴄ ᴄᴇꜱꜱ 』</b>
<blockquote>
⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}whatmusic</code> ʀᴇᴘʟʏ ᴠɪᴅᴇᴏ ᴀᴛᴀᴜ ᴍᴜꜱɪᴄ

⎆ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ:
⊶ ᴍᴇɴᴅᴇᴛᴇᴋꜱɪ ꜱᴇʙᴜᴀʜ ᴍᴜꜱɪᴋ.
</blockquote>
"""

async def upload_media(m: Message):
    media = await m.reply_to_message.download()
    try:
        ext = "unknown"
        if os.path.exists(media):
            kind = filetype.guess(media)
            if kind:
                ext = kind.extension
        
        form_data = aiohttp.FormData()
        form_data.add_field("fileToUpload", open(media, "rb"), filename=f"file.{ext}")
        form_data.add_field("reqtype", "fileupload")
        
        async with aiohttp.ClientSession() as session:
            async with session.post("https://catbox.moe/user/api.php", data=form_data) as res:
                if res.status == 200:
                    response_text = await res.text()
                    return response_text.strip()
                else:
                    return None
    except Exception as e:
        print(f"ᴇʀʀᴏʀ ꜱᴀᴀᴛ ᴍᴇɴɢᴜɴɢɢᴀʜ ᴍᴇᴅɪᴀ ᴄᴜᴋɪ: {e}")
        return None
    finally:
        if os.path.exists(media):
            os.remove(media)

@PY.UBOT("whatmusic")
async def whatmusic_handler(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.video:
        return await message.reply("ꜱɪʟᴀᴋᴀɴ ʙᴀʟᴀꜱ ᴋᴇ ꜱᴇʙᴜᴀʜ ᴠɪᴅᴇᴏ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇɴᴀʟɪ ᴍᴜꜱɪᴋɴʏᴀ ᴄᴇꜱꜱ.")
    
    msg = await message.reply("🔄 ᴍᴇɴɢᴜɴɢɢᴀʜ ᴠɪᴅᴇᴏ ᴄᴇꜱꜱ...")
    video_url = await upload_media(message)

    if not video_url:
        return await msg.edit("❌ ɢᴀɢᴀʟ ᴍᴇɴɢᴜɴɢɢᴀʜ ᴠɪᴅᴇᴏ ᴄᴜᴋɪ!")
    
    await msg.edit("🎵 ᴍᴇɴɢᴀɴᴀʟɪꜱɪꜱ ᴍᴜꜱɪᴋ ᴅᴀʟᴀᴍ ᴠɪᴅᴇᴏ ᴄᴇꜱꜱ...")
    
    response = requests.get(f"https://api.botcax.eu.org/api/tools/whatmusic?url={video_url}&apikey=045705b1")
    if response.status_code == 200:
        try:
            data = response.json()
            print("API Response:", data)
            
            if data.get("status"):
                result = data.get("result", "").strip()
                if not result or "undefined" in result.lower():
                    return await msg.edit("❌ ᴍᴜꜱɪᴋ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴅᴀʟᴀᴍ ᴠɪᴅᴇᴏ ᴄᴜᴋɪ.")
                return await msg.edit(f"**🎶 ʜᴀꜱɪʟ ᴘᴇɴɢᴇɴᴀʟᴀɴ ᴍᴜꜱɪᴋ ᴄᴇꜱꜱ:**\n```{result}```")
        except Exception as e:
            print(f"ᴇʀʀᴏʀ ᴘᴀʀꜱɪɴɢ JSON: {e}")
            return await msg.edit("❌ ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ ᴅᴀʟᴀᴍ ᴍᴇᴍᴘʀᴏꜱᴇꜱ ᴅᴀᴛᴀ API ᴄᴜᴋɪ.")
    return await msg.edit(f"❌ ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʜᴀꜱɪʟ ᴄᴜᴋɪ (Status: {response.status_code})")
