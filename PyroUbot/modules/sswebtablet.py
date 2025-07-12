import os
import datetime
import requests
from PyroUbot import *

__MODULE__ = "ꜱꜱ ᴡᴇʙ ᴛᴀʙʟᴇᴛ"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱꜱ ᴡᴇʙ ᴛᴀʙʟᴇᴛ ᴄᴇꜱꜱ 』</b>

<blockquote><b>ᴘᴇʀɪɴᴛᴀʜ :
<code>{0}ꜱꜱᴡᴇʙᴛᴀʙʟᴇᴛ</code> ʟɪɴᴋ
ᴜɴᴛᴜᴋ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴡᴇʙꜱɪᴛᴇ ᴛᴀʙʟᴇᴛ</b></blockquote>
"""

def get_ssweb_image(url):
    api_url = "https://api.botcahx.eu.org/api/tools/sstablet"
    params = {
        "url": url,
        "device": "desktop",
        "apikey": "Biyy"
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None

@PY.UBOT("sswebtablet")
async def screenshot_handler(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.reply_text("<b><i>ᴍᴀɴᴀ ᴜʀʟ ɴʏᴀ ᴄᴜᴋɪ!</i></b>")
        return

    url = args[1].strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    await message.reply_text("<b><i>ᴘʀᴏꜱᴇꜱ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴘᴀᴋᴀɪ ᴛᴀʙʟᴇᴛ ᴇʀᴅʏᴄᴇꜱꜱ ♛</i></b>")

    image_data = get_ssweb_image(url)
    if not image_data:
        await message.reply_text("<b><i>ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴄᴜᴋɪ.</i></b>")
        return

    filepath = f"img2p.jpeg"
    with open(filepath, "wb") as file:
        file.write(image_data)

    await client.send_photo(message.chat.id, filepath, caption="**__ɴɪʜ ᴄᴇꜱꜱ ɢᴀᴍʙᴀʀɴʏᴀ ꜱᴜᴅᴀʜ ᴅɪ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴘᴀᴋᴀɪ ᴛᴀʙʟᴇᴛ.__**")
    os.remove(filepath)
    
