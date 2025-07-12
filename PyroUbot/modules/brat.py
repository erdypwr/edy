import os
from PyroUbot import *
from pyrogram.enums import MessagesFilter
from pyrogram.types import *
import requests

__MODULE__ = "ʙʀᴀᴛ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʀᴀᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}brat [text]</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴛᴇxᴛ sᴇᴘᴇʀᴛɪ ᴛʀᴇɴ ᴛɪᴋᴛᴏᴋ</b></blockquote>

"""

def get_brat_image(text):
    url = f"https://api.botcahx.eu.org/api/maker/brat"
    params = {
        "text": text,
        "apikey": "045705b1"
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
        
@PY.UBOT("brat")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ /brat <ᴛᴇᴋs> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ.")
        return

    request_text = args[1]
    await message.reply_text("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ᴄᴇss...")


    image_content = get_brat_image(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ɢᴀɢᴀʟ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ. ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ ᴄᴇss")


@PY.BOT("brat")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ /brat <ᴛᴇᴋs> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ.")
        return

    request_text = args[1]
    await message.reply_text("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ᴄᴇss...")


    image_content = get_brat_image(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ɢᴀɢᴀʟ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ. ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ ᴄᴇss")
