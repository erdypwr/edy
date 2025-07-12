import requests
import random
from PyroUbot import *

def get_random_tafsir(query):
    API_URL = "https://api.botcahx.eu.org/api/islamic/tafsirsurah"
    API_KEY = "025a6ef0"

    params = {"text": query, "apikey": API_KEY}

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("status") and "result" in data:
            tafsir_list = data["result"]
            if tafsir_list:
                tafsir = random.choice(tafsir_list)
                return (
                    f"<blockquote><b>📖 **{tafsir['surah']}**\n\n</b></blockquote>"
                    f"<blockquote><b>{tafsir['tafsir']}\n\n</b></blockquote>"
                    f"<blockquote><b>🔗 [ꜱᴜᴍʙᴇʀ]({tafsir['source']})</b></blockquote>"
                )
        return "<blockquote><b><emoji id=5215204871422093648>❌</emoji> ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴛᴀꜰꜱɪʀ ʏᴀɴɢ ꜱᴇꜱᴜᴀɪ.</b></blockquote>"

    except requests.exceptions.Timeout:
        return "<blockquote><b><emoji id=5454415424319931791>⌛️</emoji> ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴡᴀᴋᴛᴜ ʜᴀʙɪꜱ. ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ.</b></blockquote>"
    except requests.exceptions.RequestException as e:
        return f"<blockquote><b><emoji id=5213205860498549992>⚠️</emoji> ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ ꜱᴀᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴛᴀꜰꜱɪʀ: {e}</b></blockquote>"

@PY.UBOT("tafsir")
async def tafsir_handler(client, message):
    if len(message.command) < 2:
        return await message.reply(
            "<blockquote><b>**__<emoji id=5213205860498549992>⚠️</emoji> ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ: `>ᴛᴀꜰꜱɪʀ <ᴋᴀᴛᴀ_ᴋᴜɴᴄɪ>`\n</b></blockquote>"
            "<blockquote><b>ᴄᴏɴᴛᴏʜ: `>ᴛᴀꜰꜱɪʀ ᴍᴜʜᴀᴍᴍᴀᴅ`__**</b></blockquote>"
        )

    query = " ".join(message.command[1:])
    await message.reply("<blockquote><b><i><emoji id=4967797089971995307>🔍</emoji> ꜱᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴛᴀꜰꜱɪʀ...</i></b></blockquote>")

    tafsir_text = get_random_tafsir(query)

    await message.reply(tafsir_text, disable_web_page_preview=True)
