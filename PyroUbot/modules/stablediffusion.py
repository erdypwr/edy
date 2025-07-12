import os
from PyroUbot import *
import requests

__MODULE__ = "ꜱᴛᴀʙʟᴇᴅɪғғᴜꜱɪᴏɴ"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴛᴀʙʟᴇᴅɪғғᴜꜱɪᴏɴ ᴄᴇꜱꜱ 』</b>
<blockquote><b>
⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}ꜱᴅ</code> ᴛᴇxᴛ
⊶ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴛᴇxᴛ.</b></blockquote>
"""

def get_giraffe_image(text):
    url = "https://api.botcahx.eu.org/api/search/stablediffusion"
    params = {
        "text": text,
        "apikey": f"moire"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
                                                       
@PY.UBOT("sd")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("<b><i>ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ /ꜱᴛᴀʙʟᴇᴅɪғғᴜꜱɪᴏɴ <ᴛᴇᴋꜱ> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴄᴇꜱꜱ</i></b>.")
        return

    request_text = args[1]
    await message.reply_text("<b><i>ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ᴄᴇꜱꜱ</i></b>...")

    image_content = get_giraffe_image(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ɢᴀɢᴀʟ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴄᴜᴋɪ. ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ ᴄᴇꜱꜱ")