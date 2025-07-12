from pyrogram import Client, filters
import requests
import asyncio
from PyroUbot import *

__MODULE__ = "ᴛᴡɪᴛᴛᴇʀ"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴡɪᴛᴛᴇʀ ᴄᴇꜱꜱ 』</b>
<blockquote><b>
⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}twit</code> ʟɪɴᴋ ᴠɪᴅᴇᴏ ᴛᴡɪᴛᴛᴇʀ
⊶ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜꜱɪᴄ ʏᴀɴɢ ᴅɪ ɪɴɢɪɴᴋᴀɴ.</b></blockquote>
"""

async def get_twitter_video(url):
    api_url = f"https://api.botcahx.eu.org/api/dowloader/twitter?url={url}&apikey=025a6ef0"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("status"):
            video_urls = data["result"]["url"]
            hd_url = video_urls[0].get("hd") if video_urls else None
            sd_url = video_urls[1].get("sd") if len(video_urls) > 1 else None
            return hd_url or sd_url
    return None

@PY.UBOT("twit")
async def twitter_download(client, message):
    if len(message.command) < 2:
        await message.reply_text("ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: /twitter <ʟɪɴᴋ_ᴛᴡɪᴛᴛᴇʀ>")
        return

    twitter_url = message.command[1]
    msg = await message.reply_text("ᴍᴇɴɢᴀᴍʙɪʟ ᴠɪᴅᴇᴏ, ʜᴀʀᴀᴘ ᴛᴜɴɢɢᴜ ᴄᴇꜱꜱ...")

    video_url = await get_twitter_video(twitter_url)

    if video_url:
        await msg.edit("ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ᴄᴇꜱꜱ...")
        await message.reply_video(video_url, caption="ʙᴇʀɪᴋᴜᴛ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴇʟᴜ ᴍɪɴᴛᴀ.")
    else:
        await msg.edit("ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴠɪᴅᴇᴏ ᴄᴜᴋɪ. ᴘᴀꜱᴛɪᴋᴀɴ ʟɪɴᴋ ʙᴇɴᴀʀ ᴀᴛᴀᴜ ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ ᴄᴇꜱꜱ.")
