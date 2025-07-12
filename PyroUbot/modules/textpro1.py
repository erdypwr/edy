import os
import requests
from PyroUbot import *

# Masukkan API Key ᴇʟᴜ di sini
API_KEY = "Btz-bxwol"  # Ganti dengan API key yang benar

__MODULE__ = "ᴛᴇxᴛᴘʀᴏ 1"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇxᴛᴘʀᴏ 1 ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴇꜱꜱ 』</b>

<blockquote><b>ᴘᴇʀɪɴᴛᴀʜ : <code>ꜱᴜɴʟɪɢʜᴛ</code>
ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴅᴇɴɢᴀɴ ᴇꜰᴇᴋ ꜱᴜɴʟɪɢʜᴛ.</b></blockquote>
<blockquote><b>ᴘᴇʀɪɴᴛᴀʜ : <code>ɴɪɢʜᴛꜱᴛᴀʀꜱ</code>
ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴅᴇɴɢᴀɴ ᴇꜰᴇᴋ ɴɪɢʜᴛꜱᴛᴀʀꜱ.</b></blockquote>
"""

def fetch_image(api_url, text):
    """
    ꜰᴜɴɢꜱɪ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ɢᴀᴍʙᴀʀ ᴅᴀʀɪ ᴀᴘɪ
    """
    params = {"text": text, "apikey": API_KEY}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            print("ʀᴇꜱᴘᴏɴꜱ ʙᴜᴋᴀɴ ɢᴀᴍʙᴀʀ:", response.text)  # Debugging
            return None
    except requests.exceptions.RequestException as e:
        print(f"ᴇʀʀᴏʀ ꜰᴇᴛᴄʜɪɴɢ ɪᴍᴀɢᴇ: {e}")  # Debugging jika ada kesalahan
        return None

async def process_image_command(client, message, api_url, command_name):
    """
    ꜰᴜɴɢꜱɪ ᴜᴍᴜᴍ ᴜɴᴛᴜᴋ ᴍᴇɴᴀɴɢᴀɴɪ ᴘᴇʀɪɴᴛᴀʜ ᴘᴇᴍʙᴜᴀᴛᴀɴ ɢᴀᴍʙᴀʀ
    """
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text(f"<b><i>ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ /{command_name} <ᴛᴇᴋꜱ> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ.</i></b>")
        return

    request_text = args[1]
    await message.reply_text("<b><i>ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ ᴄᴇꜱꜱ...</i></b>")

    image_content = fetch_image(api_url, request_text)
    if image_content:
        temp_file = f"{command_name}.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)
        await message.reply_photo(photo=temp_file)
        os.remove(temp_file)
    else:
        await message.reply_text("ɢᴀɢᴀʟ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴄᴜᴋɪ. ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ ᴄᴇꜱꜱ")

# Handler untuk setiap perintah
@PY.UBOT("sunlight")
async def sunlight_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/ephoto/sunlight"
    await process_image_command(client, message, api_url, "sunlight")

@PY.UBOT("nightstars")
async def nightstars_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/ephoto/nightstars"
    await process_image_command(client, message, api_url, "nightstars")
