from pyrogram import Client, filters
import requests
from PyroUbot import *

__MODULE__ = "ᴄᴀᴘᴄᴜᴛ ᴅʟ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴀᴘᴄᴜᴛ ᴅʟ ᴄᴇꜱꜱ 』</b>
<blockquote>
⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}ᴄᴀᴘᴅʟ</code> ʟɪɴᴋ

⎆ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ:
⊶ ᴅᴏᴡɴʟᴏᴀᴅ ᴛᴇᴍᴘʟᴀᴛᴇ ᴄᴀᴘᴄᴜᴛ.
</blockquote></b></blockquote>

"""


@PY.UBOT("capdl")
async def capcut_download(client, message):
    if len(message.command) < 2:
        await message.reply_text("ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: /ᴄᴀᴘᴅʟ [ᴜʀʟ ᴄᴀᴘᴄᴜᴛ]")
        return
    
    url = message.command[1]
    processing_msg = await message.reply_text("🔄 ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ, ʜᴀʀᴀᴘ ᴛᴜɴɢɢᴜ ᴄᴇss...")
    
    response = requests.get(f"https://api.botcahx.eu.org/api/download/capcut?url={url}&apikey=045705b1")
    data = response.json()
    
    if not data.get("status"):
        await processing_msg.edit_text("❌ ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ. ᴘᴀsᴛɪᴋᴀɴ ᴜʀʟ ᴠᴀʟɪᴅ ᴄᴇss")
        return
    
    video_url = data["result"]["video"]
    thumbnail_url = data["result"]["thumbnail"]
    title = data["result"].get("short_title", "ᴄᴀᴘᴄᴜᴛ ᴠɪᴅᴇᴏ")
    author = data["result"].get("author", {}).get("name", "ᴜɴᴋɴᴏᴡɴ")
    
    await message.reply_video(
        video=video_url,
        thumb=thumbnail_url,
        caption=f"**{title}**\n👤 ᴘᴇᴍʙᴜᴀᴛ: {author}\n🔗 [ꜱᴜᴍʙᴇʀ]({url})",
    )
    
    await processing_msg.delete()