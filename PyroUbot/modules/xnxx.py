import requests
import os
from PyroUbot import *

__MODULE__ = "xɴxx"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ xɴxx cess 』</b>
<blockquote><b>
ᴘᴇʀɪɴᴛᴀʜ :
<code>{0}xnxx</code> kata pencarian
Mendownload Video Yang Di Inginkan.</b></blockquote>
"""

@PY.UBOT("xnxx")
async def random_bokep(client, message):
    try:
        query = message.text.split()[1:]
        if not query:
            await message.reply("<emoji id=5215204871422093648>❌</emoji> ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: `.xnxx [ᴋᴀᴛᴀ ᴋᴜɴᴄɪ]`\n\nᴄᴏɴᴛᴏʜ: `.xnxx japanese teacher` ᴀᴛᴀᴜ `.xnxx bokep`")
            return
        search_query = " ".join(query[:4])
        
        status_msg = await message.reply(f"<emoji id=4967797089971995307>🔍</emoji> ᴍᴇɴᴄᴀʀɪ ʙᴏᴋᴇᴘ ᴜɴᴛᴜᴋ: **{search_query}**...")

        api_url = f"https://api.botcahx.eu.org/api/search/xnxx?query={search_query}&apikey=045705b1"
        
        response = requests.get(api_url)
        response.raise_for_status()
        api = response.json()

        results = api.get('result', [])
        if not results:
            await status_msg.edit(f"<emoji id=5215204871422093648>❌</emoji> ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ʜᴀꜱɪʟ ᴜɴᴛᴜᴋ: **{search_query}**")
            return

        data = results[0]

        capt = f"卍 **ʜᴀꜱɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ: {search_query}**\n\n"
        capt += f"  ◦ **ᴛɪᴛʟᴇ** : {data.get('title', 'N/A')}\n"
        capt += f"  ◦ **ᴠɪᴇᴡꜱ** : {data.get('views', 'N/A')}\n"
        capt += f"  ◦ **ǫᴜᴀʟɪᴛʏ** : {data.get('quality', 'N/A')}\n"
        capt += f"  ◦ **ᴅᴜʀᴀᴛɪᴏɴ** : {data.get('duration', 'N/A')}\n"
        capt += f"  ◦ **[🔗 ʟɪɴᴋ ]({data.get('link', 'N/A')})**\n"

        await status_msg.edit(f"📥 ᴍᴇɴɢᴜɴᴅᴜʜ ᴠɪᴅᴇᴏ ᴅᴀʀɪ: **{data.get('title', 'N/A')}**...")

        dl_url = f"https://api.botcahx.eu.org/api/download/xnxxdl?url={data['link']}&apikey=045705b1"
        dl_response = requests.get(dl_url)
        dl_response.raise_for_status()
        dl_data = dl_response.json()
        video_url = dl_data.get('result', {}).get('url')

        if not video_url:
            await status_msg.edit("<emoji id=5215204871422093648>❌</emoji> ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ URL ᴠɪᴅᴇᴏ.")
            return

        video_path = "video.mp4"

        await status_msg.edit("📥 ꜱᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴᴅᴜʜ ᴠɪᴅᴇᴏ, ʜᴀʀᴀᴘ ᴛᴜɴɢɢᴜ...")
        with requests.get(video_url, stream=True) as vid_res:
            vid_res.raise_for_status()
            with open(video_path, "wb") as f:
                for chunk in vid_res.iter_content(chunk_size=8192):
                    f.write(chunk)

        await status_msg.edit("📤 ᴍᴇɴɢᴜɴɢɢᴀʜ ᴠɪᴅᴇᴏ ᴋᴇ ᴛᴇʟᴇɢʀᴀᴍ...")
        
        await client.send_video(message.chat.id, video_path, caption=capt)
        os.remove(video_path)

        await status_msg.delete()

    except requests.exceptions.RequestException as e:
        await message.reply(f"<emoji id=5215204871422093648>❌</emoji> ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ ꜱᴀᴀᴛ ᴍᴇɴɢᴀᴋꜱᴇꜱ API: {str(e)}")
    except Exception as e:
        await message.reply(f"<emoji id=5215204871422093648>❌</emoji> ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ: {str(e)}")
        
