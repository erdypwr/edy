# Copyright (C) 2020 Aidil Aryanto.
# All rights reserved.
import asyncio
import glob
import os
import subprocess
import time
from PyroUbot import *

__MODULE__ = "ɴɢᴀᴍʙɪʟʟᴀɢᴜ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɴɢᴀᴍʙɪʟʟᴀɢᴜ ᴄᴇꜱꜱ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}lagu</code> [ᴛᴇᴋꜱ/ʙᴀʟᴀꜱ ᴋᴇ ᴛᴇᴋꜱ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ʟᴀɢᴜ ᴅᴀʀɪ ʏᴏᴜᴛᴜʙᴇ (ᴍᴘ3)

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}vlagu</code> [ᴛᴇᴋꜱ/ʙᴀʟᴀꜱ ᴋᴇ ᴛᴇᴋꜱ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ʟᴀɢᴜ ᴅᴀʀɪ ʏᴏᴜᴛᴜʙᴇ (ᴍᴘ4)
</blockquote>
"""

def yt_search(query):
    import requests
    from bs4 import BeautifulSoup
    url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for vid in soup.find_all('a', attrs={'id': 'video-title'}):
        video_link = f"https://www.youtube.com{vid.get('href')}"
        return video_link
    return None

@PY.UBOT(["lagu"])
async def _(c, m):
    query = m.text.split(None, 1)[1] if len(m.command) > 1 else (m.reply_to_message.text if m.reply_to_message else None)
    if not query:
        return await m.reply("<b>ᴍᴀꜱᴜᴋᴋᴀɴ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ ʟᴀɢᴜ ᴀᴛᴀᴜ ʙᴀʟᴀꜱ ᴋᴇ ᴛᴇᴋꜱ!</b>")
    proses = await m.reply("<b>ᴍᴇɴᴄᴀʀɪ ʟᴀɢᴜ...</b>")
    video_link = yt_search(query)
    if not video_link:
        return await proses.edit("<b>ʟᴀɢᴜ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b>")
    await proses.edit("<b>ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ʟᴀɢᴜ...</b>")
    command = f"yt-dlp -x --add-metadata --embed-thumbnail --no-progress --audio-format mp3 {video_link}"
    os.system(command)
    mp3_files = glob.glob("*.mp3")
    if not mp3_files:
        return await proses.edit("<b>ɢᴀɢᴀʟ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ʟᴀɢᴜ!</b>")
    mp3_file = mp3_files[0]
    await m.reply_document(mp3_file, caption=f"<b>ʟᴀɢᴜ ᴅᴀʀɪ: {query}</b>")
    await proses.delete()
    os.remove(mp3_file)

@PY.UBOT(["vlagu"])
async def _(c, m):
    query = m.text.split(None, 1)[1] if len(m.command) > 1 else (m.reply_to_message.text if m.reply_to_message else None)
    if not query:
        return await m.reply("<b>ᴍᴀꜱᴜᴋᴋᴀɴ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ ʟᴀɢᴜ ᴀᴛᴀᴜ ʙᴀʟᴀꜱ ᴋᴇ ᴛᴇᴋꜱ!</b>")
    proses = await m.reply("<b>ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ʟᴀɢᴜ...</b>")
    video_link = yt_search(query)
    if not video_link:
        return await proses.edit("<b>ᴠɪᴅᴇᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b>")
    await proses.edit("<b>ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ...</b>")
    command = f"yt-dlp -f 'bestvideo[filesize<50M]+bestaudio/best[filesize<50M]' --no-progress --merge-output-format mp4 {video_link}"
    os.system(command)
    mp4_files = glob.glob("*.mp4")
    if not mp4_files:
        return await proses.edit("<b>ɢᴀɢᴀʟ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ!</b>")
    mp4_file = mp4_files[0]
    await m.reply_document(mp4_file, caption=f"<b>ᴠɪᴅᴇᴏ ᴅᴀʀɪ: {query}</b>")
    await proses.delete()
    os.remove(mp4_file)
