from pyrogram import Client, filters
import requests
from PyroUbot import *

__MODULE__ = "ᴛɪᴋᴛᴏᴋ sᴇᴀʀᴄʜ"  # sudah tinycaps
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛɪᴋᴛᴏᴋ sᴇᴀʀᴄʜ ᴄᴇꜱꜱ 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ttsearch</code> 
   <i>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴠᴛ ʏᴀɴɢ ᴅɪ ᴘᴇʀɪɴᴛᴀʜᴋᴀɴ.</i></blockquote>
"""

API_KEY = "045705b1"

@PY.UBOT("tiktoksearch|tts|ttsearch")
async def tiktok_search(client, message):
    if len(message.command) < 2:
        return await message.reply("<blockquote><b>ɢᴜɴᴀᴋᴀɴ: `.tiktoksearch query`</b></blockquote>")

    query = " ".join(message.command[1:])
    proses_msg = await message.reply("<blockquote><b>🔍 **sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴛɪᴋᴛᴏᴋ ᴄᴇꜱꜱ...**</b></blockquote>")

    url = f"https://api.botcahx.eu.org/api/search/tiktoks?query={query}&apikey={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return await proses_msg.edit("<blockquote><b>❌ **ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ ᴅᴀʀɪ API.**</b></blockquote>")

    data = response.json()
    if not data.get("status") or not data.get("result", {}).get("data"):
        return await proses_msg.edit("<blockquote><b>❌ **ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴠɪᴅᴇᴏ ᴜɴᴛᴜᴋ query ᴛᴇʀꜱᴇʙᴜᴛ.**</b></blockquote>")

    video = data["result"]["data"][0]
    caption = (
        f"<blockquote><b>🎬 **ᴊᴜᴅᴜʟ:** {video['title']}\n</b></blockquote>"
        f"<blockquote><b>🌍 **ᴡɪʟᴀʏᴀʜ:** {video['region']}\n</b></blockquote>"
        f"<blockquote><b>🎵 **ᴍᴜꜱɪᴋ:** {video['music_info']['title']} - {video['music_info']['author']}\n</b></blockquote>"
        f"<blockquote><b>▶ **ᴊᴜᴍʟᴀʜ ᴘᴜᴛᴀʀ:** {video['play_count']}\n</b></blockquote>"
        f"<blockquote><b>❤️ **ʟɪᴋᴇ:** {video['digg_count']}\n</b></blockquote>"
        f"<blockquote><b>💬 **ᴋᴏᴍᴇɴᴛᴀʀ:** {video['comment_count']}\n</b></blockquote>"
        f"<blockquote><b>🔗 [ᴛᴏɴᴛᴏɴ ᴅɪ ᴛɪᴋᴛᴏᴋ]({video['play']})</b></blockquote>"
    )

    await proses_msg.edit("<blockquote><b>📥 **ᴍᴇɴɢᴜɴᴅᴜʜ ᴠɪᴅᴇᴏ ᴄᴇꜱꜱ...**</b></blockquote>")

    await message.reply_video(video["play"], caption=caption)

    await proses_msg.delete()
