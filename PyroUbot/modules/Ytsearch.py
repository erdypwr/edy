import os
import requests
from PyroUbot import *

# Masukkan API Key ᴇʟᴜ di sini
API_KEY = "045705b1"  # Ganti dengan API key yang benar

__MODULE__ = "ʏᴛsᴇᴀʀᴄʜ"
__HELP__ = """
📚 <b> 『 ʏᴛꜱᴇᴀʀᴄʜ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴇꜱꜱ 』</b>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>ytsearch</code>
🦠 ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴅɪ ʏᴏᴜᴛᴜʙᴇ ʙᴇʀᴅᴀꜱᴀʀᴋᴀɴ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ.</b></blockquote>
"""

def fetch_youtube(api_url, query):
    """
    ꜰᴜɴɢꜱɪ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ʜᴀꜱɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ ᴅᴀʀɪ API ʏᴏᴜᴛᴜʙᴇ
    """
    params = {"query": query, "apikey": API_KEY}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        # Memeriksa apakah respons berisi hasil pencarian
        data = response.json()
        if "result" in data:
            return data["result"]
        else:
            print("ᴛɪᴅᴀᴋ ᴀᴅᴀ ʜᴀꜱɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ ᴅᴀʟᴀᴍ ʀᴇꜱᴘᴏɴꜱᴇ ᴄᴜᴋɪ:", data)
            return None
    except requests.exceptions.RequestException as e:
        print(f"ᴇʀʀᴏʀ ꜰᴇᴛᴄʜɪɴɢ ʏᴏᴜᴛᴜʙᴇ ʀᴇꜱᴜʟᴛꜱ: {e}")
        return None

async def process_youtube_command(client, message, api_url, command_name):
    """
    ꜰᴜɴɢꜱɪ ᴜᴍᴜᴍ ᴜɴᴛᴜᴋ ᴍᴇɴᴀɴɢᴀɴɪ ᴘᴇʀɪɴᴛᴀʜ ᴘᴇɴᴄᴀʀɪᴀɴ ʏᴏᴜᴛᴜʙᴇ
    """
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text(f"<b><i>ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ /{command_name} <ᴋᴀᴛᴀ ᴋᴜɴᴄɪ> ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴅɪ ʏᴏᴜᴛᴜʙᴇ ᴄᴇꜱꜱ.</i></b>")
        return

    query = args[1]
    await message.reply_text("<b><i>🔍 ꜱᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ᴄᴇꜱꜱ...</i></b>")

    results = fetch_youtube(api_url, query)
    if results:
        # Mengirimkan hasil pencarian sebagai daftar
        response_text = (
            "<b><emoji id=5841235769728962577>📹</emoji> ʜᴀꜱɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ ᴠɪᴅᴇᴏ ᴅɪ ʏᴏᴜᴛᴜʙᴇ ᴄᴇꜱꜱ:</b>\n\n"
        )
        for idx, result in enumerate(results[:5], start=1):  # Menampilkan hingga 5 hasil saja
            title = result.get("title", "ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴊᴜᴅᴜʟ")
            link = result.get("url", "ᴛɪᴅᴀᴋ ᴀᴅᴀ ʟɪɴᴋ")
            duration = result.get("duration", "ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")
            views = result.get("views", "ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")
            response_text += (
                f"<b><emoji id=5841243255856960314>{idx}.</emoji> {title}</b>\n"
                f"<b><emoji id=5843952899184398024>⏱️</emoji> ᴅᴜʀᴀꜱɪ:</b> {duration}\n"
                f"<b><emoji id=5841243255856960314>👁‍🗨</emoji> ᴠɪᴇᴡꜱ:</b> {views}\n"
                f"<b><emoji id=5841235769728962577>🔗</emoji> ʟɪɴᴋ:</b> <a href='{link}'>ᴛᴏɴᴛᴏɴ ᴠɪᴅᴇᴏ</a>\n\n"
            )
        await message.reply_text(response_text, disable_web_page_preview=True)
    else:
        await message.reply_text("ɢᴀɢᴀʟ ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴄᴜᴋɪ. ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ ᴄᴇꜱꜱ.")

# Handler untuk perintah ytsearch
@PY.UBOT("ytsearch")
async def youtube_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/search/yts"
    await process_youtube_command(client, message, api_url, "ytsearch")
